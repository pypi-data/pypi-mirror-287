from datetime import datetime

from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.tree import Tree as rTree
from rich.pretty import pprint
from rich.rule import Rule

MAX_ROWS = 30

# Define color schemes
COLOR_SCHEMES = {    
    'truecolor': {
        'info': 'rgb(137,209,255)',
        'title': 'bold rgb(137,209,255)',
        'header': 'italic rgb(137,209,255)',
        'line': 'rgb(137,209,255)',
        'var': 'rgb(0,112,242)',
        'error': 'rgb(210,10,10)',
        'warn': 'rgb(255,201,51)',
        'item': 'rgb(137,209,255)',
        'bullet': 'rgb(0,112,242)',
        'treelevel': ['bold white', 'rgb(27,144,255)', 'rgb(137,209,255)', 'rgb(209,239,255)', 'rgb(209,239,255)', 
                    'rgb(209,239,255)', 'rgb(209,239,255)', 'rgb(209,239,255)', 'rgb(209,239,255)', 'rgb(209,239,255)', 
                    'rgb(209,239,255)', 'rgb(209,239,255)']
    },
    '256colors': {
        'info': 'color(87)',
        'title': 'bold color(27)',
        'header': 'italic color(27)',
        'line': 'color(27)',
        'var': 'color(87)',
        'error': 'color(196)',
        'warn': 'color(190)',
        'item': 'color(87)',
        'bullet': 'color(27)',
        'treelevel': ['bold color(7)', 'color(27)', 'color(39)', 'color(45)', 'color(87)', 'color(87)', 'color(87)', 
                    'color(87)', 'color(87)', 'color(87)', 'color(87)', 'color(87)']
    },
    'basic': {
        'info': 'cyan',
        'title': 'bold blue',
        'header': 'italic blue',
        'line': 'blue',
        'var': 'cyan',
        'error': 'red',
        'warn': 'yellow',
        'item': 'cyan',
        'bullet': 'blue',
        'treelevel': ['bold white', 'blue', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 
                    'cyan', 'cyan', 'cyan', 'cyan', 'cyan']

    },
    'mono': {
        'info': 'white',
        'title': 'bold white',
        'header': 'italic white',
        'line': 'white',
        'error': 'white',
        'warn': 'white',
        'item': 'white',
        'bullet': 'white',
        'treelevel': ['bold white', 'white', 'white', 'white', 'white', 'white', 'white', 
                    'white', 'white', 'white', 'white', 'white']

    }
}

# Initialize color scheme
actual_scheme = '256colors'
cc = COLOR_SCHEMES[actual_scheme]
def set_color_scheme(scheme):
    global actual_scheme,cc
    if scheme in COLOR_SCHEMES:
        actual_scheme = scheme
        cc = COLOR_SCHEMES[actual_scheme]
    else:
        actual_scheme='basic'
        cc = COLOR_SCHEMES[actual_scheme]

def error(msg: str) -> None:
    rprint(f"[{cc['error']}]{msg}")

def warning(msg: str) -> None:
    rprint(f"[{cc['warn']}]{msg}")

def info(info: str, msg=None) -> None:
    if msg:
        rprint(f"[{cc['info']}]{info}: [{cc['var']}]{msg}")
    else: 
        rprint(f"[{cc['info']}]{info}")

def line(length=80, char='─'):
    rprint(f"[{cc['line']}]{char * length}")

def title(msg: str, length=80,line=True,char='─') -> None:
    rprint(f"[bold {cc['title']}]\n{msg}")
    rprint(f"[{cc['line']}]{char * length}")

def bullet_list(items: list, title=None) -> None:
    if title:
        rprint(f"[{cc['title']}]{title}")
    for i in items:
        rprint(f"[{cc['bullet']}]\u2022  [{cc['item']}]{i}")
    print('\n')

def dict2tree(data, tree, level=1, title="Tree") -> rTree:
    if not data:
        return tree
    elif isinstance(data, list):
        for i in data:
            tree.add(f"[{cc['treelevel'][level]}]{i}[/]")
    elif isinstance(data, dict):
        for k, v in data.items():
            stree = tree.add(f"[{cc['treelevel'][level]}]{k}[/]")
            dict2tree(v,stree,level+1)
    else:
        tree.add(f"[{cc['treelevel'][level]}]{data}[/]")
    
def tree(data_dict,title = None)-> None:
    if title == None:
        if len(data_dict) == 1:
            title = list(data_dict.keys())[0]
        else:
            title = 'root'
    tree = rTree(title)
    dict2tree(data_dict, tree )
    rprint('\n',tree, '\n')
    
def print_tree(tree,name='shares')-> None:
    rtree = rTree(f"[{cc['treelevel'][0]}]{name}[/]")
    dict2tree(rtree, tree)
    rprint('\n',rtree, '\n')


# def print_dataframe(df: pd.DataFrame, title='DataFrame', max_rows = MAX_ROWS) -> Table:
#     max_rows = max_rows if df.shape[0] > MAX_ROWS else df.shape[0]
#     table = Table(title=title, header_style=header_style, title_style=cc['header'])
#     for c in df.columns:
#         table.add_column(c, justify="left", style=cc['info'], no_wrap=True)
#     for _, row in df.tail(max_rows).iterrows():
#         vals = [ str(r) for r in row.values]
#         table.add_row(*vals)
#     rprint(table)

def table(columns: list, lists:list, title='Lists', max_rows = MAX_ROWS) -> None:
    max_rows = max_rows if len(lists) > MAX_ROWS else len(lists)
    table = Table(title=title, header_style=cc['header'], title_style=cc['header'] )
    for c in columns:
        table.add_column(c, justify="left", style=cc['info'], no_wrap=False)
    for row in lists[:max_rows]:
        vals = [ str(r) for r in row]
        table.add_row(*vals)
    rprint('\n',table,'\n')

def dictionary(data: dict, title='Dictionary', columns=['Key','Value'],max_rows = MAX_ROWS) -> None:
    max_rows = max_rows if len(data) > MAX_ROWS else len(data)
    table = Table(title=title, header_style=cc['header'], title_style=cc['header'] )
    for c in columns:
        table.add_column(c, justify="left", style=cc['info'], no_wrap=False)
    for k,v  in data.items():
        table.add_row(str(k),str(v))
    rprint('\n',table,'\n')

def listdicts(data:list, title='Dictionaries', columns=['Key','Value'],max_rows = MAX_ROWS) -> None:
    max_rows = max_rows if len(data) > MAX_ROWS else len(data)
    table = Table(title=title, header_style=cc['header'], title_style=cc['header'] )
    table.add_column(columns[0], justify="left", style=cc['info'], no_wrap=False)
    table.add_column(columns[1], justify="left", style=cc['info'], no_wrap=False)
    for i, d in enumerate(data):
        table.add_row(str(i),"")
        table.add_section()
        for k,v  in d.items():
            table.add_row(str(k),str(v))
    rprint('\n',table,'\n')

def delta_schema(delta_table)->None:
    if delta_table:
        fields = delta_table.schema().fields
        fields = [ (i+1, f.name,f.type.type, f.nullable) for i, f in enumerate(fields)]
        table(["Seq","Field",'Dtype','Nullable'],fields,'Data Types')

def delta_metadata(version, metadata)->None:
    if metadata:
        table = Table(title=f"Metadata", header_style=cc['header'], title_style=cc['header'] )
        table.add_column('Key', justify="left", style=cc['info'], no_wrap=False)
        table.add_column('Value', justify="left", style=cc['info'], no_wrap=False)
        table.add_row('version',str(version))
        table.add_row('name',metadata.name)
        table.add_row('description',metadata.description)   
        table.add_row('id',str(metadata.id)) 
        table.add_row('partition columns',str(metadata.partition_columns)) 
        table.add_row('created at',datetime.fromtimestamp(int(metadata.created_time/1000)).isoformat())
        table.add_section()
        for k, v in metadata.configuration.items(): 
            table.add_row(k, v) 
        rprint('\n',table)

def delta_history(history: dict) -> None:
    table = Table(title=f"History", header_style=cc['header'], title_style=cc['header'] )
    table.add_column('Version', justify="left", style=cc['info'])
    table.add_column('Timestamp', justify="left", style=cc['info'])
    table.add_column('Operation', justify="left", style=cc['info'])
    table.add_column('Client Version', justify="left", style=cc['info'])
    for h in history:
        table.add_row(str(h['version']),datetime.fromtimestamp(int(h['timestamp']/1000)).isoformat(),
                      h['operation'], h['clientVersion'])
    rprint('\n', table)


def print_share_metadata(table_path, metadata):
    mds = metadata['metadata']

    for m, md in enumerate(mds):
        rprint(Rule(title=f"Metadata Version: {md['version']}/{metadata['last_schema_version']}", style=crule))
        rprint(f"[{cc['header']}]{table_path}:\n")
        table1 = Table(title=f"Metadata", header_style=cc['header'], title_style=cc['header'] )
        table1.add_column('Metadata', justify="left", style=cc['info'], no_wrap=False)
        table1.add_column('Value', justify="left", style=cc['info'], no_wrap=False)

        table1.add_row("Version",str(md['version']))
        if 'enableChangeDataFeed' in md['configuration']:
            table1.add_row("CDF enabled",md['configuration']['enableChangeDataFeed'])
        if 'size' in md:
            table1.add_row("Size",str(md['size']))
        if 'partitionColumns' in md:
            table1.add_row("Partition Columns",str(md['partitionColumns']))
        rprint(table1,"\n")
        table2 = Table(title=f"Schema", header_style=cc['header'], title_style=cc['header'] )
        table2.add_column('Column Name', justify="left", style=cc['info'], no_wrap=False)
        table2.add_column('Data Type', justify="left", style=cc['info'], no_wrap=False)
        table2.add_column('Nullable', justify="left", style=cc['info'], no_wrap=False)
        for c,v in md['schema'].items():
            table2.add_row(c,v['type'],str(v['nullable']))
        rprint(table2)

def print_ds_metadata(table_path, metadata):
    table1 = Table(title=f"Metadata", header_style=cc['header'], title_style=cc['header'] )
    table1.add_column('Metadata', justify="left", style=cc['info'], no_wrap=False)
    table1.add_column('Value', justify="left", style=cc['info'], no_wrap=False)

    table1.add_row("Version",str(metadata['version']))
    table1.add_row("Version",str(metadata['version']))
    if 'enableChangeDataFeed' in metadata['configuration']:
        table1.add_row("CDF enabled",metadata['configuration']['enableChangeDataFeed'])
    if 'size' in metadata:
        table1.add_row("Size",str(metadata['size']))
    if 'partitionColumns' in metadata:
        table1.add_row("Partition Columns",str(metadata['partitionColumns']))
    rprint(table1,"\n")
    table2 = Table(title=f"Schema", header_style=cc['header'], title_style=cc['header'] )
    table2.add_column('Column Name', justify="left", style=cc['info'], no_wrap=False)
    table2.add_column('Data Type', justify="left", style=cc['info'], no_wrap=False)
    table2.add_column('Nullable', justify="left", style=cc['info'], no_wrap=False)
    for c,v in metadata['schema'].items():
        table2.add_row(c,v['type'],str(v['nullable']))
    rprint(table2)

def print_request_info(method, endpoint, path, headers, params={},data={}):
    table = Table(title="Request Info", header_style=cc['header'], title_style=cc['header'],
                  expand=True)
    table.add_column("Key", justify="left", style=cc['info'])
    table.add_column("Value", justify="left", style=cc['info'],overflow="fold")
    table.add_row("method", method)
    table.add_row("endpoint", endpoint)
    table.add_row("resource path", path)
    table.add_section()
    table.add_row("Headers",'')
    for k, v in headers.items():
        if k == 'Authorization':
            v = v[: 50] + '...'
        table.add_row(k,str(v))
    if params: 
        table.add_section()
        table.add_row("Parameter",'')
        for k, v in params.items():
            table.add_row(k,str(v))
    if data:
        table.add_section()
        table.add_row("Data",'')
        for k, v in data.items():
            table.add_row(k,str(v))

    table.add_section()
    headers = ','.join(f"{k}:{v}" for k, v in headers.items())
    curl = f"curl -X {method} {endpoint}{path} -H \"{headers}\" --cert {params['cert']} --key {params['key']}"
    table.add_row("CURL",curl)
    
    rprint(table, '\n')
