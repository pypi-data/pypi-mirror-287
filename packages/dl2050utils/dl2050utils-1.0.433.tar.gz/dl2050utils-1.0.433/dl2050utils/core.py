from typing import *
import traceback
import re
from collections import OrderedDict
from collections.abc import Iterable, Generator
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
from tqdm.notebook import tqdm

# ################################################################################
# Helper functions
# ################################################################################

def A(a=None): return np.array([]).astype(np.int32) if a is None else np.array(a)
def W(a): return np.where(a)[0]

def is_numeric_str(e):
    if type(e)!=str: return False
    return e.lstrip('-+').replace('.','',1).isdigit()

def is_iter(o):
    return isinstance(o, (Iterable,Generator)) and getattr(o,'ndim',1)

def is_array(x):
    return hasattr(x,'__array__') or hasattr(x,'iloc')

def lol_to_l(lol):
    return [e for l in lol for e in l]

def try_call(f, args=[], kwargs={}, LOG=None, label='', label2='', debug=False):
    try:
        return f(*args, **kwargs)
    except Exception as exc:
        if LOG is not None:
            if debug:
                LOG(4, 0, label=label, label2='EXCEPTION',
                    msg={'EXCEPTION':str(exc),'TRACEBACK':traceback.format_exc()})
            else:
                LOG(4, 0, label=label, label2=f'{label2} EXCEPTION', msg=str(exc))
        return -1

# ################################################################################
# checks
# checks input formats and limits the input size
# usefull for input passed as requests payload to avoid too large data
# ################################################################################

def check_float(e):
    if type(e) not in [str, int, float]: return None
    s = str(e)[:32]
    if is_numeric_str(s):
        return float(s)
    return None

def check_int(e):
    f = check_float(e)
    if f is None:
        return None
    return int(f)

def check_str(e, n=1024):
    if type(e) not in [str, int, float]: return None
    return str(e)[:n]

def check(e, n=1024):
    """
        Check input and accept only int, float or bool
        Limit input size to n if string
    """
    if type(e) in [int, float, bool]:
        return e
    if type(e)==str:
        return str(e)[:n]
    return None

# ################################################################################
# listify
# ################################################################################

def listify(o):
    """ Transforms input into a list. """
    if o is None: return []
    if isinstance(o, list): return o
    if type(o)==np.ndarray: return list(o)
    if isinstance(o, str) or is_array(o): return [o]
    if is_iter(o): return list(o)
    return [o]

# ################################################################################
# oget
# ################################################################################

def oget(o, fs, default_=None):
    """
        Extracts a deeper subelement of a dict base on a list of hierarchical attributes.
        Sub-elements may be dicts or lists.
    """
    if o is None or fs is None: return default_
    for f in listify(fs):
        if type(o)==dict and f in o:
            o = o[f]
        elif type(o)==list and (type(f)==int or np.issubdtype(f, np.integer)) and f<len(o):
            o = o[f]
        else:
            return default_
    return o

# ################################################################################
# re
# ################################################################################

def xre(r, s):
    """
        Returns regex pattern in string if found, otherwise None.
        Example: r = xre('(DS_Store)',str(s))
    """
    if type(r)!=str or type(s)!=str: return None
    m = re.search(r, s)
    return m.group(1) if m else None

# ################################################################################
# LRUCache
# ################################################################################

class LRUCache:
    def __init__(self, size):
        self.size,self.cache = size,OrderedDict()

    def get(self, key, load_callback=None, **kwargs):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        elif load_callback is not None:
            value = load_callback(key, **kwargs)
            self.put(key, value)
            return value
        else:
            return -1
        
    async def get_async(self, key, load_callback=None, **kwargs):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        elif load_callback is not None:
            value = await load_callback(key, **kwargs)
            self.put(key, value)
            return value
        else:
            return -1
            
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.size:
            self.cache.popitem(last=False)
        self.cache[key] = value

# ################################################################################
# parallel
# ################################################################################

def parallel(f, a, nprocs=16):
    """
    Apply function f to array a, splitting the process through nprocs parallel processes.
    Splits the array a into nprocs chunks.
    Returns the combined results for all processes.
    Important Considerations:
        Global Variables: Each process has its own memory space; changes in one process don't affect the others.
        Pickling: Function f and input arguments must be pickleable.
        Performance: The overhead of creating and managing multiple processes can affect performance for very small tasks.
    """
    # Split a into nprocs chunks
    chunks = np.array_split(a, nprocs)
    results = []
    # Use ProcessPoolExecutor for parallel processing
    with ProcessPoolExecutor(max_workers=nprocs) as executor:
        # Submit all tasks
        future_to_chunk = {executor.submit(f, chunk): chunk for chunk in chunks}
        with tqdm(total=len(future_to_chunk), desc="Processing") as pbar:
            # Process results as they complete
            for future in as_completed(future_to_chunk):
                chunk = future_to_chunk[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as exc:
                    print(f'Chunk with {len(chunk)} elements generated an exception: {exc}')
                pbar.update(1)
    return results

# ################################################################################
# LexIdx
# ################################################################################
        
class LexIdx():
    def __init__(self, sz=8):
        self.base_chars = [chr(i) for i in range(48,58)]+[chr(i) for i in range(97,123)]+[chr(i) for i in range(65,10)]
        self.base_d = {self.base_chars[i]:i for i,e in enumerate(self.base_chars)}
        self.base = len(self.base_chars)
        self.sz,self.step = sz,1000000
    def encode(self, n):
        enc = ""
        while n > 0:
            n,r = divmod(n,self.base)
            enc = self.base_chars[r] + enc
        return enc.zfill(self.sz)
    def decode(self, b):
        b = b[::-1]
        n = 0
        for i,c in enumerate(b):
            n += self.base_d[c]*(self.base**i)
        return n
    def interpolate(self, b1, b2):
        n1,n2 = self.decode(b1),self.decode(b2)
        return self.encode(int((n1+n2)/2))
    def next(self, b):
        n = self.decode(b)
        return self.encode(n+self.step)

# l = LexIdx()
# b1,b2 = l.encode(1000000),l.encode(2000000)
# l.decode(l.interpolate(b1,b2))
# l.decode(l.next(b2))

# ################################################################################
# Etc (not yet ready, to be tested)
# ################################################################################

def setify(o):
    return o if isinstance(o,set) else set(listify(o))

def uniqueify(x, sort=False):
    res = list(OrderedDict.fromkeys(x).keys())
    if sort: res.sort()
    return res

class L():
    def __init__(self, items): self.items = listify(items)
    def __getitem__(self, idx):
        try: return self.items[idx]
        except TypeError:
            if isinstance(idx[0],bool):
                assert len(idx)==len(self) # bool mask
                return [o for m,o in zip(idx,self.items) if m]
            return [self.items[i] for i in idx]
    def __len__(self): return len(self.items)
    def __iter__(self): return iter(self.items)
    def __setitem__(self, i, o): self.items[i] = o
    def __delitem__(self, i): del(self.items[i])
    def __repr__(self):
        res = f'{self.__class__.__name__} ({len(self)} items)\n{self.items[:10]}'
        if len(self)>10: res = res[:-1]+ '...]'
        return res
    def append(self,o): return self.items.append(o)
    def remove(self,o): return self.items.remove(o)
    def unique(self): return L(dict.fromkeys(self).keys())
    def sort(self, key=None, reverse=False): return self.items.sort(key=key, reverse=reverse)
    def reverse(self ): return self.items.reverse()

_camel_re1 = re.compile('(.)([A-Z][a-z]+)')
_camel_re2 = re.compile('([a-z0-9])([A-Z])')
def camel2snake(name):
    s1 = re.sub(_camel_re1, r'\1_\2', name)
    return re.sub(_camel_re2, r'\1_\2', s1).lower()

def compose(x, funcs, *args, order_key='_order', **kwargs):
    key = lambda o: getattr(o, order_key, 0)
    for f in sorted(listify(funcs), key=key): x = f(x, **kwargs)
    return x

def ifnone(a, b): return b if a is None else a

def check_list_str(e, sz=64, n=1024):
    """
        Enforce input to be list and check_str all elements
        Limits list lenght to sz and every element size to n
    """
    if type(e)!=list: return None
    return [check_str(e1,n) for e1 in e[:sz]]

def check_dict(e, keys=[], n=1024):
    """
        Returns the input to be dict with only the attributes deffined in keys
        Every attribute must be int, float, bool or str
        String attributes are enforce to max lengh of n
    """
    if type(e)!=dict:
        return None
    d = {}
    for k in keys:
        if k not in e:
            continue
        if type(e[k]) in [bool,int,float]:
            d[k] = e[k]
        elif is_numeric_str(e[k]):
            v = check_float(e[k])
            if int(v)==v:
                v = int(v)
            d[k] = v
        else:
            d[k] = check_str(e[k], n=n)
    return d
