Behavior observed with Python 3.8:

```
$ python3 -m asdf
in asdf.__init__, __name__ is asdf and __package__ is asdf
in asdf.__main__, __name__ is __main__ and __package__ is asdf
   and sys.args contains ['.../test_python_package/asdf/__main__.py']
   and asdf is in sys.modules? True
```
