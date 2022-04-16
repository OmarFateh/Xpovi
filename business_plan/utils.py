import random
import string


def generate_random_string(length=10):
    """
    Generate a random alphanumeric string of letters and digits of a given fixed length.
    """
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def generate_unique_name(instance, new_name=None):
    """Generate a unique name of given instance."""
    # check if the given arguments have a value of new name.
    # if yes, assign the given value to the name field. 
    if new_name is not None:
        name = new_name
    # if not, generate a name of a random string.
    else:
        name = generate_random_string()
    # get the instance class. 
    Klass = instance.__class__
    # check if there's any item with the same name.
    qs_exists = Klass.objects.filter(name=name).exists()
    # if yes, generate a new name of a random string and return recursive function with the new name.
    if qs_exists:
        new_name = generate_random_string()
        return generate_unique_name(new_name=new_name)
    return name