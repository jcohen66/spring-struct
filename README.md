# spring-struct

#Usage

### Python Script
Running as script with Python
````
python3 spring-struct.py com.example.demo
````

### Executable Script 
Running as script from prompt 
````
pip3 install -e /Users/Jonathan.Cohen/PycharmProjects/spring_struct
````

### Executable 
Running as executable from prompt after 'pip install'
````
spring_struct your.base.package
````


# Output 

Produces Spring packages under the specified root package/path.

Produces empty application.properties and static and templates 
directories under resources.

````
.
├── mvnw
├── mvnw.cmd
├── pom.xml
├── spring-struct.py
└── src
    ├── main
    │   ├── java
    │   │   └── com
    │   │       └── example
    │   │           └── demo
    │   │               ├── demoApplication.java
    │   │               ├── config
    │   │               ├── controllers
    │   │               ├── model
    │   │               ├── repositories
    │   │               └── services
    │   └── resources
    │       ├── application.properties
    │       ├── static
    │       └── templates
    └── test
        └── java
            └── com
                └── example
                    └── demo
                        └── demoApplicationTests.java
                        
```` 

#Installation

To install with pip (make sure to replace path with your source path):

````
pip3 install -e /Users/Jonathan.Cohen/PycharmProjects/spring_struct
````