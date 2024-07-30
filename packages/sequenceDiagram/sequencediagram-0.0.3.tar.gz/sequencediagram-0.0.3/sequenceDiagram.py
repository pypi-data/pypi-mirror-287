import functools
import inspect
import os


traces=[]

def resetseq():
    traces=[]
def writehtml(file_path):
    global traces
    try:
        with open(file_path,'w') as file:
            html=html_string.replace("<<seqdiag>>","\n".join(traces))
            file.write(html)
    except :
        print("Error in ")

def sequenceDiagram(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        caller_frame = inspect.stack()[1]
        
        caller_class_name = None
        if 'self' in caller_frame.frame.f_locals:
            caller_class_name = caller_frame.frame.f_locals['self'].__class__.__name__

        called_class_name = args[0].__class__.__name__ if args else None

        if not caller_class_name:
            caller_class_name = removechars(os.path.basename(caller_frame.filename))

        if not called_class_name:
            called_class_name = removechars(os.path.basename(inspect.getfile(func)))

        caller_fn_name_str = removechars(caller_frame.function)
        called_fn_name_str = removechars(func.__name__)

        args_repr = transformInput(args)
        kwargs_repr = transformInput(kwargs.items())

        signature = ", ".join(args_repr + kwargs_repr)
        traces.append(f"{caller_class_name}->>{called_class_name}:{caller_fn_name_str}()--{removechars(called_fn_name_str)}({signature})")
        result = func(*args, **kwargs)
        resultrepr=transformInput(result)
        resultrepr=", ".join(resultrepr)
        traces.append(f"{called_class_name}-->{caller_class_name}:{resultrepr}")
        return result

    return wrapper

def isiter(obj):
    if isinstance(obj,str):
        return False
    try:
        iter(obj)
        return True
    except:
        return False

def transformInput(args):
    listre=[]
    if not (isiter(args)):
        args=[args]
    for a in args:
        if isinstance(a,int) or isinstance(a,float) or isinstance(a,bool):
            listre.append(a)
        elif isinstance(a,str):
            if len(a)>10:
                a=removechars(a)
                a=a[:10]
            listre.append(a)
        elif isinstance(a, object):
            listre.append(removechars(str(a.__class__.__name__)))
    
    listre = [element for element in listre if element is not None]
    return listre

def removechars(namestr):
    namestr=namestr.replace(">","").replace("<","").replace(":","")
    return namestr

html_string="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sequence Diagram</title>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({ startOnLoad: true });
    </script>
</head>
<body>
    <!-- Your Mermaid diagram -->
    <div class="mermaid">
        sequenceDiagram
        <<seqdiag>>
    </div>
</body>
</html>"""