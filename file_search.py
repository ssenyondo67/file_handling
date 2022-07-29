# this will demo strate the application of factory method using python
# we are imagining each category is stored in diferent database theirfore will require different access properties

class ITFiles:

    def __init__(self) -> None:
          pass
    
    def retrieve_file(self):
        pass
    
    def __str__(self) -> str:
        return 'IT'

class EconomicsFiles:

    def __init__(self) -> None:
          pass
    
    def retrieve_file(self):
        pass
    
    def __str__(self) -> str:
        return 'Economics'

class MechanicsFiles:

    def __init__(self) -> None:
          pass
    
    def retrieve_file(self):
        pass
    
    def __str__(self) -> str:
        return 'Mechanics'

class ArtFiles:

    def __init__(self) -> None:
          pass
    
    def retrieve_file(self):
        pass
    
    def __str__(self) -> str:
        return 'Art'


def Factory(category):

    categories={
        'it':ITFiles,
        'economics':EconomicsFiles,
        'art':ArtFiles,
        'mechanics':MechanicsFiles
        
    }
    return categories[category]()

if __name__=='__main__':
    cat=input('Enter category: ')
    print(Factory(cat))
    