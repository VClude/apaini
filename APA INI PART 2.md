# APA INI PART 2

## JUnit Annotation
* `@Test` annotation specifies that method is the test method.

* `@Test(timeout=1000)` annotation specifies that method will be failed if it takes longer than 1000 milliseconds (1 second).

* `@BeforeClass` annotation specifies that method will be invoked only once, before starting all the tests.

* `@Before` annotation specifies that method will be invoked before each test.

* `@After` annotation specifies that method will be invoked after each test.

* `@AfterClass` annotation specifies that method will be invoked only once, after finishing all the tests.
## Execution order JUnit

* Method annotated with `@BeforeClass`
* Method annotated with `@Before`
* First method annotated with `@Test` i.e. `test1()`.
* Method annotated with `@After`
* Method annotated with `@Before`
* Second method annotated with `@Test` i.e. `test2()`.
* Method annotated with `@After`
* Method annotated with `@AfterClass`


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
## cron syntax
|syntax|desc|
|--- |--- |
|\*|any value|
|,|value list separator|
|-|range of values|
|/|step values|
|@yearly|(non-standard)|
|@annually|(non-standard)|
|@monthly|(non-standard)|
|@weekly|(non-standard)|
|@daily|(non-standard)|
|@hourly|(non-standard)|
|@reboot|(non-standard)|
## @runwith parameterized `org.junit.runners.Parameterized.Parameters;`
Parameterized tests allow a developer to run the same test over and over again using different values. 
### step
* Annotate test class with `@RunWith(Parameterized.class)`.

* Create a public static method annotated with `@Parameters` that returns a Collection of Objects (as Array) as test data set.

* Create a public constructor that takes in what is equivalent to one "row" of test data.

* Create an instance variable for each "column" of test data.

* Create your test case(s) using the instance variables as the source of the test data.
### Example
```java
...
@RunWith(Parameterized.class)
public class CalcTest {
    private int a,b,expected;
    public CalculatorTest(int a, int b, int expected){
        this.a=a;
        this.b=b;
        this.expected=expected;
    }
    ...
    
    @Test
    public void testAdd(){
    Calculator instance = new Calculator();
    int actual = instance.add(a,b);
    Assert.assertEquals(expected, actual);
    }
@Parameters
    public static Collection<Integer[]> getParameters(){
    Integer [][]inputArr;
    
    ...
```

## Stub
A stub is a controllable replacement for an existing dependency (or collaborator) in the system. By using a stub, you can test your code without dealing with the dependency directly.

**example stub code**
```java
interface Service {
    String doSomething();
}

class ServiceStub implements Service {
    public String doSomething(){
        return "my stubbed return";
    }
}
```
## JWebUnit
```java
import static net.sourceforge.jwebunit.junit.JWebUnit.*;

public class ExampleWebTestCase {
	
    @Before
    public void prepare() {
        setBaseUrl("http://localhost:8080/test");
    }

    @Test
    public void test1() {
        beginAt("home.xhtml"); //Open the browser on http://localhost:8080/test/home.xhtml
        clickLink("login");
        assertTitleEquals("Login");
        setTextField("username", "test");
        setTextField("password", "test123");
        submit();
        assertTitleEquals("Welcome, test!");
    }
}
```
## IDataSet `org.dbunit.dataset.IDataSet`
* `getDataSet()` : generate data from various source to IDataSet Object
* `FlatXMLDataSetBuilder()` : build data from xml format
example xml format
```xml
<?xml version='1.0' encoding='UTF-*'?>
<dataset>
	<studentinfo StudentID="001" StudentName="awe"/>
</dataset>
```
example test via db
```java
public void insertData(URL dataSetUrl) throws Exception {
    System.out.println("Insert test data.");
    final IDataSet dataSet = loadDataSet(dataSetUrl);
    final DatabaseConnection connection = new DatabaseConnection(
            getDBconnection());
    DatabaseOperation.INSERT.execute(connection, dataSet);
}
```
## JUnit Report
* **Tools** : Maven
* **Plugin** : Surefire
## Summary
|Tests|Errors|Failures|Skipped|Success Rate|Time|
|--- |--- |--- |--- |--- |--- |
|Total Test functions|Error in function|Failures in Function (Assert not true)|skipped|percentage of total testfunc-failfunc/testfunc|time elapsed|
### Package List
|Package|Tests|Errors|Failures|Skipped|Success Rate|Time|
|--- |--- |--- |--- |--- |--- |--- |
|exampletestpkg|3|0|0|0|100%|0.01|
### exampletestpkg
|Class|Tests|Errors|Failures|Skipped|Success Rate|Time|
|--- |--- |--- |--- |--- |--- |--- |
|exampleclass|3|0|0|0|100%|0.01|
### Test Class
#### exampleclass
| | |
|--- |--- |
|test1func|0.001|
|test2func|0.001|
|test3func|0.001|
## Common issue
