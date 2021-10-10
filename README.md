[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/shabalin13/Arithmetic-PvP">
    <img src="logo.png" alt="Logo" width="300" height="171">
  </a>

  <p align="center">
    Multiplayer verbal counting game
    <br />
    <a href="https://github.com/shabalin13/Arithmetic-PvP/tree/main/Documentation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/shabalin13/Arithmetic-PvP/issues">Report Bug</a>
    ·
    <a href="https://github.com/shabalin13/Arithmetic-PvP/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->

  <h2 style="display: inline-block">Table of Contents</h2>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#for-whom">For Whom</a></li>
      </ul>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#requirements">Requirements</a>
    </li>
    <li>
      <a href="#design">Design</a>
      <ul>
        <li><a href="#diagrams">Diagrams</a></li>
      </ul>
      <ul>
        <li><a href="#solid-principles-and-design-patterns">SOLID principles and Design patterns</a></li>
      </ul>
    </li>
    <li><a href="#architecture">Architecture</a></li>
    <li>
       <a href="#demo">Demo</a>
      <ul>
        <li><a href="#demo-screens">Demo screens</a></li>
      </ul>
      <ul>
        <li><a href="#demonstration">Demonstration</a></li>
      </ul>
    </li>
    <li><a href="#code">Code</a></li>
    <li><a href="#contacts">Contacts</a></li>
  </ol>




<!-- ABOUT THE PROJECT -->
## About The Project

Arithmetic PvP is a verbal counting online game. Players compete in calculating various expressions, starting from primitive ones, such as 2+2, ending with extremely hard containing several-digit numbers. There is also a single-player mode, where you can run the endless mode and constantly improve your skill, or play campain which has levels of increasing complexity. 

### For Whom
Play our game if you want to:

* Improve your arithmetic skills
* Find new friends with same interests
* Compete!


### Built With

* [Bootstrap](https://getbootstrap.com/)
* [Vue.js](https://vuejs.org/)
* [Django REST API](https://www.django-rest-framework.org/)



<!-- GETTING STARTED -->
## Getting Started

1) Download the Node.js from [source](https://nodejs.org/en/download/)
2) Clone the repo
    ```
    git clone https://github.com/shabalin13/Arithmetic-PvP.git
    ```
3) Go to the backend directory (Arithmetic-PvP/Arithmetic_PvP_backend)
4) Install all Requirements
    ```
    pip install -r requirements.txt
    ```
5) Start the local server
    ```
    python3 manage.py runserver
    ```
6) Go to the frontend directory (Arithmetic-PvP/frontend)
7) Install NPM packages
    ```
    npm install
    ```
8) Start Vue.js
    ```
    npm run serve
    ```

## Requirements

All development documentation can be found here [Requirements](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Requirements.pdf)

### Content of the Requirements

1.  Glossary
2.  Business Goals and Objectives
3.  Roles and responsibilities
4.  Functional requirements
5.  User Stories
6.  Non-Functional Requirements
7.  Software Development plan


## Design

### Diagrams

* [Class Diagram](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Class_diagram.png) for Django Models that are connected to database. So this is core of our backend side. However other parts of our project are not completely based on objects. So class diagram is not useful in our case.
* [Sequence Diagram](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Sequence_diagram.png)
* [Use Case Diagram](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Use_case_diagram.png)

### SOLID principles and Design patterns

* *Single responsibility* - All classes have only one responsibility (only one purpose).
* *Open-closed* - There are many examples of using open/closed principle in our project. For example, permissions for views are easily modifiable changing only one line before the function. Another example is the room and task constructors. Constructors for these models are implemented inside model managers and one can easily add new constructor. We will definitely use it when creating new task generators.
* *Liskov substitution* - This principle is applicable in Models.
* *Interface segregation* - Large interfaces are splitted into smaller ones. Implementing classes concerned only about the methods that are of interest to them. There is no request that are used rarely or not used at all. So there is nothing to segregate in our case.
* *Dependency inversion* - All classes use other classes through interfaces.

## Architecture

All diagrams about architecture of application can be found by following links below

* [Static View](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Static_diagram.png)
* [Dynamic View](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Dynamic_diagram.png)

## Demo

### Demo screens

![Demo](https://github.com/shabalin13/Arithmetic-PvP/blob/main/Documentation/Demo-screens.png)

### Demonstration

You can see video demonstration of our app on [YouTube](https://www.youtube.com/watch?v=YBOpn10ter0)


## Code

* **Static analyzer results:**
Here is the link of our linter worlflow: [lint.yml](https://github.com/shabalin13/Arithmetic-PvP/actions/workflows/linter.yml). ([NOTICE]   All file(s) linted successfully with no errors detected)
* **Testing:**
At this stage of development, we only performed manual testing. Since our project is still in the development stage, we think that it makes no sense to add tests for code that changes quite often.


<!-- CONTACTS -->
## Contacts

Collaborators - Kamil Agliullin, Aidar Khuzin, Dmitrii Shabalin, Evgeny Petrashko

Project Link: [https://github.com/shabalin13/Arithmetic-PvP](https://github.com/shabalin13/Arithmetic-PvP)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/shabalin13/Arithmetic-PvP.svg?style=for-the-badge
[contributors-url]: https://github.com/shabalin13/Arithmetic-PvP/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shabalin13/Arithmetic-PvP.svg?style=for-the-badge
[forks-url]: https://github.com/shabalin13/Arithmetic-PvP/network/members
[stars-shield]: https://img.shields.io/github/stars/shabalin13/Arithmetic-PvP.svg?style=for-the-badge
[stars-url]: https://github.com/shabalin13/Arithmetic-PvP/stargazers
[license-shield]: https://img.shields.io/github/license/shabalin13/Arithmetic-PvP.svg?style=for-the-badge

