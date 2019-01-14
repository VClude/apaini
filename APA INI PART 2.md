# APA INI PART 2

## JUnit Annotation
* `@Test` annotation specifies that method is the test method.

* `@Test(timeout=1000)` annotation specifies that method will be failed if it takes longer than 1000 milliseconds (1 second).

* `@BeforeClass` annotation specifies that method will be invoked only once, before starting all the tests.

* `@Before` annotation specifies that method will be invoked before each test.

* `@After` annotation specifies that method will be invoked after each test.

* `@AfterClass` annotation specifies that method will be invoked only once, after finishing all the tests.

## Type of Testing
Test Strategies :
* **Blackbox Testing** Test overall software functionality, does not cover each statement.
* **Whitebox Testing** Test every statement and condition given in the code

Once strategies are decided, testing can be done at various level :
* **UNIT TESTING** is a level of software testing where individual units/ components of a software are tested. The purpose is to validate that each unit of the software performs as designed.
* **Integration testing** (sometimes called integration and testing, abbreviated I&T) is the phase in software testing in which individual software modules are combined and tested as a group(sometimes called integration and testing, abbreviated I&T) is the phase in software testing in which individual software modules are combined and tested as a group.
* **System testing** is performed on a complete, integrated system. It allows checking system's compliance as per the requirements. It tests the overall interaction of components. It involves load, performance, reliability and security testing.
* **Acceptance testing** is a test conducted to find if the requirements of a specification or contract are met as per its delivery. Acceptance testing is basically done by the user or customer. However, other stockholders can be involved in this process.
* **Regression testing** is the process of testing changes to computer programs to make sure that the older programming still works with the new changes.
