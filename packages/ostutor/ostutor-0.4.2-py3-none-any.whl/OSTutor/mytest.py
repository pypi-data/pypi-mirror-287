def test_parse_man():
    import os
    from src.data import Parse
    from pprint import pprint
    current_dir = os.getcwd()
    # Command_document_template
    file  = os.path.join(current_dir, '..', 'Command_document_template.txt')
    data = Parse().parseMan(file)
    # print(data['DESCRIPTION'])
    pprint(data)
    return data

def test_store():
    from src.data import Storage
    import os
    from src.data import collection
    from pprint import pprint
    from src.data import Parse
    current_dir = os.getcwd()
    file = collection.Collection().collectMan('ostutor2', 'user', 'ostutor2')
    print(file)
    file  = os.path.join(current_dir, '..', 'ostutor.txt')
    print(file)
    data = Parse().parseMan(file)
    print(data)
    # Storage().Store(file)
    # current_dir = os.getcwd()
    # file  = os.path.join(current_dir, '..', 'Command_document_template.txt')
    # print(file)
    # data = Parse().parseMan(file)
    # Storage().Store(file)
test_store()