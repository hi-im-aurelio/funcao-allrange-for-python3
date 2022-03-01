## funcao-allrange-for-python3
>Create rangebased on lists or values of the range itself. Range any type. Can you imagine?

### WARNING!!!
>THIS MODULE DID NOT COME TO REPLACE THE RANGE() FUNCTION<br>
> **NOTE:** So much so that they can work or be implemented together and at the same time in your code.


For reasons of not being able to select the beginning and the end (if it is, until the jump) of values ​​in an already existing list, I created the allrange.
Basically it does what the name says. But giving more control over dynamic and static lists.
From an existing list or even one dynamically created by range(x, y), I can do the same as a range() would do in, for example:

In a range() I would do:
~~~python
for num in range(1, 5): print(num)

#or

numbers = range(1, 5)
for num in numbers: print(num)
~~~

>See that in range() I select exactly the beginning and end of these numeric values.<br>
>Now with allrange():


##### For elements of type string.
~~~python
names = ["Felipe", "Paulo", "Lopéz", "Carla"]
for name in allrange(2, 4, names): print(name)

INPUT:
* Paul
* Lopez
* Carla
~~~

##### For elements of type int.
~~~python
numbers = [1, 2, 3, 4, 5, 6]
for num in allrange(2, 4, numbers): print(num)


INPUT:
* 2
* 3
* 4
~~~

##### For elements of all kinds.
>Which is where the name of the function came from. "all range"
~~~python
dynamicList = ["Python", 2, "PHP", "C#", 23, 55, [1, "JS"], {"Your favorite language:": "Python"}, (1, 3, 4, 5 )]
for dynlist in allrange(1, 9, dynamicList): print(dynlist)

INPUT:
* Python
* 2
* PHP
* C#
* 23
* 55
* [1, 'JS']
* {'Your favorite language:': 'Python'}
* (1, 3, 4, 5)
~~~

##### You can even do the following using the range() function together with allrange()
~~~python
for x in allrange(2, 5, range(1, 11)): print(x)

INPUT:
* 2
* 3
* 4
* 5
~~~
> ##### That is, you have great power to generate and control data more dynamically, even using the range() function.
