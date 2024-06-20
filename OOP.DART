import 'dart:io';


abstract class Animal {
  String name;

  Animal(this.name);

  void speak();
}

class Dog extends Animal {
  Dog(String name) : super(name);

  @override
  void speak() {
    print('$name says Woof!');
  }
}


class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void speak() {
    print('$name says Meow!');
  }
}



abstract class Vehicle {
  void accelerate();
}


class Car implements Vehicle {
  @override
  void accelerate() {
    print('Car is accelerating!');
  }

  void start() {
    print('Car started!');
  }
}



class Employee {
  String name;
  int age;

  Employee(this.name, this.age);

  @override
  String toString() {
    return 'Employee: $name, Age: $age';
  }
}

void main() {
  
  var employeeData = File('employee_data.txt').readAsStringSync();
  var parts = employeeData.split(',');
  var employee = Employee(parts[0], int.parse(parts[1]));

  print(employee); 

  void printNumbers(int n) {
    for (var i = 1; i <= n; i++) {
      print(i);
    }
  }
5
  printNumbers(5); 
}
