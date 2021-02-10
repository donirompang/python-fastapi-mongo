import bson

def generate_id() -> str:
    '''
    Generate Object ID as string
    '''
    return str(bson.objectid.ObjectId())

def validate_id(id: str) -> bool:
    '''
    Validate Object ID
    '''
    return bson.objectid.ObjectId.is_valid(id)