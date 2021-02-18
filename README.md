# AirBnB_clone

## Authors

    Lucho Patino
    Esteban Castano

![image1](hbnb.png)

This is the first phase of the AirBnB_clone project. In this case the objective its to build a basic console
that takes arguments from the user to build, modify or delete instances of the classes available and saves it to a file name **file.json**.

The following image shows the scope of the first phase in comparison to the global project:

![image1](phase1.png)

To start the console you can use two ways:

1. Using python3 to execute the file

```
    python3 console.py
```

2. Making the file console.py with permissions to be an executable and running the program

```
    chmod u+x console.py
    ./console.py
```

Once the file is executed, the user will be greeted with the following prompt:

```
    (base) EZ/.../AirBnB_clone/$ ./console.py
    (hbnb)
```

Now you are inside the console. Here you the following commands available:

- **quit** and **EOF** -> to exit the program
- **help** -> To show the documentation of each method.
- **create** -> Creates a new instance of a class and saves it in a file.
- **show** -> Prints the string representation of an instance based on the class name and _id_
- **destroy** -> Deletes an instance based on the class name and **id** and save the change in a file.
- **all** -> Prints all string representation of all instances based or not on the class name.
- **update** -> Updates an instance based on the class name and id by adding or updating attribute and save the change in a file.

Using the command **help** on the console shows the command available and to show us the documentation of each command we use the selected command after the method **help**, like the following shows:

```
    (base) EZ/.../AirBnB_clone/$ ./console.py
    (hbnb)help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)help create
    Creates a new instance of the
            input class and prints the id of the
            new instance.
            Example on console-> create User

    (hbnb)
```

The classes available in this stage of the project are the following:

- **User** -> Class that have the attributes _email_, _password_, _first_name_, _last_name_.
- **State** -> Class that have the attribute _name_.
- **City** -> Class that have the attributes _name_ and _state_id_
- **Amenity** -> Class that have the attribute _name_.
- **Place** -> Class that have the attributes _city_id_, _user_id_, _name_ ,_description_ ,_number_rooms_ ,_number_bathrooms_, _max_guest_, _price_by_nigth_, _latitude_, _longitude_, _amenity_ids_.
- **Review** -> Class that have the attributes _place_id_, _user_id_, _text_.

An example of how to create instances with several of the classes available are as follow:

```
    (hbnb)create User
    abfd2b87-34b7-402e-9e34-92138af48783
    (hbnb)create City
    53246df7-d070-4242-bb80-af6042b13f9f
    (hbnb)create Place
    f9bfdad6-1133-4b09-84a8-0ee0d2724453
    (hbnb)create State
    47135fc6-b62d-4a26-a378-60b7fbd98dbb
```

As shown, each time an instance is created, the console outputs the id of the instance and that id is unique for each instance. When there is a change, the file is updated. In this case the file has the following information:

```
{"User.abfd2b87-34b7-402e-9e34-92138af48783": {"id": "abfd2b87-34b7-402e-9e34-92138af48783", "created_at": "2021-02-18T14:32:03.416878", "updated_at": "2021-02-18T14:32:03.416912", "__class__": "User"}, "City.53246df7-d070-4242-bb80-af6042b13f9f": {"id": "53246df7-d070-4242-bb80-af6042b13f9f", "created_at": "2021-02-18T14:35:53.851789", "updated_at": "2021-02-18T14:35:53.851820", "__class__": "City"}, "Place.f9bfdad6-1133-4b09-84a8-0ee0d2724453": {"id": "f9bfdad6-1133-4b09-84a8-0ee0d2724453", "created_at": "2021-02-18T14:36:10.695885", "updated_at": "2021-02-18T14:36:10.695951", "__class__": "Place"}, "State.47135fc6-b62d-4a26-a378-60b7fbd98dbb": {"id": "47135fc6-b62d-4a26-a378-60b7fbd98dbb", "created_at": "2021-02-18T14:37:05.897266", "updated_at": "2021-02-18T14:37:05.897311", "__class__": "State"}}
```

Each instance shows the id, the time in which it was created and updated it and the name of the class.

There is at least to way to execute the commands, for example, if we want to show an user with an id, this can be
done as follows:

```
(base) EZ/.../AirBnB_clone/$ ./console.py
(hbnb)all
["[User] (abfd2b87-34b7-402e-9e34-92138af48783) {'id': 'abfd2b87-34b7-402e-9e34-92138af48783', 'created_at': datetime.datetime(2021, 2, 18, 14, 32, 3, 416878), 'updated_at': datetime.datetime(2021, 2, 18, 14, 32, 3, 416912)}", "[City] (53246df7-d070-4242-bb80-af6042b13f9f) {'id': '53246df7-d070-4242-bb80-af6042b13f9f', 'created_at': datetime.datetime(2021, 2, 18, 14, 35, 53, 851789), 'updated_at': datetime.datetime(2021, 2, 18, 14, 35, 53, 851820)}", "[Place] (f9bfdad6-1133-4b09-84a8-0ee0d2724453) {'id': 'f9bfdad6-1133-4b09-84a8-0ee0d2724453', 'created_at': datetime.datetime(2021, 2, 18, 14, 36, 10, 695885), 'updated_at': datetime.datetime(2021, 2, 18, 14, 36, 10, 695951)}", "[State] (47135fc6-b62d-4a26-a378-60b7fbd98dbb) {'id': '47135fc6-b62d-4a26-a378-60b7fbd98dbb', 'created_at': datetime.datetime(2021, 2, 18, 14, 37, 5, 897266), 'updated_at': datetime.datetime(2021, 2, 18, 14, 37, 5, 897311)}"]
(hbnb)show User abfd2b87-34b7-402e-9e34-92138af48783
[User] (abfd2b87-34b7-402e-9e34-92138af48783) {'id': 'abfd2b87-34b7-402e-9e34-92138af48783', 'created_at': datetime.datetime(2021, 2, 18, 14, 32, 3, 416878), 'updated_at': datetime.datetime(2021, 2, 18, 14, 32, 3, 416912)}
(hbnb)User.show("abfd2b87-34b7-402e-9e34-92138af48783")
[User] (abfd2b87-34b7-402e-9e34-92138af48783) {'id': 'abfd2b87-34b7-402e-9e34-92138af48783', 'created_at': datetime.datetime(2021, 2, 18, 14, 32, 3, 416878), 'updated_at': datetime.datetime(2021, 2, 18, 14, 32, 3, 416912)}
(hbnb)
```

Here you can see that with the command all we can see all the instances that are store in the file. Then let's say we want the console to show us the information of the class user
with an specific id, this can be done like this:

```
    (hbnb)show User abfd2b87-34b7-402e-9e34-92138af48783
    (hbnb)User.show("abfd2b87-34b7-402e-9e34-92138af48783")
```

It can be seen that both ways outputs the same result.
