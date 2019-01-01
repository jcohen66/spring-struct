# spring-struct

Usage:

````
python3 spring-struct.py com.example.demo
````
Produces Spring packages under the specified root package/path.

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