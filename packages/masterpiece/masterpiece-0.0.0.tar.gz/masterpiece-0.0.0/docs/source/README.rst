Welcome to MasterPiece Framework
================================


Project Status and Current State
--------------------------------

This is the initial commit of the project. At this stage, the framework is in its early development phase.

Here's what is currently available:

* Package Infrastructure: The basic Python package setup is in place, configured with pyproject.toml.
* Early Drafts: Initial versions of the two core base classes have been implemented 'MasterPiece' and 'Group'.
  
Insights and suggestions are invaluable as we continue to develop and refine the framework.

In this current state, you might call it merely a mission, rather than masterpiece, but I'm
working hard to turn it into a masterpiece! 



Goals
-----

The primary goal of this framework is to provide a minimal yet robust set of general-purpose base classes designed
to streamline the development of new software in Python.  The key objectives of this framework include:

* Robusness: Minimal yet robust API providing the developer with 100% control.
* First-Time Excellence: The aim is to build a robust and reliable framework that is correct and efficient from the start,
  eliminating the need for disruptive changes or backward compatibility issues in future releases.
* Abstraction: Provide a layer of abstraction to shield the API from the impacts of external code, including
  third-party libraries and APIs. 



Design
------

The design patterns employed to achieve our goals include:

* Object-Oriented Paradigm: Employing object-oriented principles to promote code reuse, encapsulation, and modularity.
* Factory Method Pattern: Decoupling implementations from their interfaces to simplify object creation and enhance flexibility.
* Layered Design Pattern: Promoting separation of concerns and reusability by organizing code into distinct layers.
* Plugin API: Enabling extensibility and customization through a well-defined plugin interface for easy integration of additional features.
* Serialization: Facilitating seamless conversion between data formats and object representations.
* Easy Configuration: Simplifying setup and management through startup arguments and configuration files.


If you appreciate these design concepts, you've come to the right place!

A framework designed with these principles deserves more than just "objects" — let's call
them "masterpieces". This term reflects commitment to fine-grained modular design ("pieces") and
adds a touch of humor with "Master".

Just as all creatures on Earth share a common ancestor, all components in this framework trace their lineage
back to this foundational anchestor named "masterpiece" ... (okay, perhaps a bit dramatic).


Install
-------

1. To install:

   `pip install masterpiece`.

This installs all the dependencies as well, I hope.

   


Developer Documentation
-----------------------

After several hours (okay, days), Sphinx finally generates something. It will require a
few more hours (okay, days) of effort to produce something really usable.



Special Thanks
--------------

My ability to translate my architecture ideas into Python is greatly due to the generous support of one
extraordinary gentleman: [Mahi.fi](https://mahi.fi). His support and encouragement have been
invaluable in bringing this project to life. Thank you!
