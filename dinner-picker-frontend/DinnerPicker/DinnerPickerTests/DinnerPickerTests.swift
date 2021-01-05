import Foundation
import XCTest
@testable import DinnerPicker

class DinnerPickerTests: XCTestCase {
    override func setUp() {
        super.setUp()
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }
    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }
}

class DataManagerTests: XCTestCase {
    var dataManager: DataManager!
    override func setUp() {
        super.setUp()
        dataManager = DataManager()
    }
    // func loadJsonFrom(fileNamed fileName: String) -> NSDictionary {
    //     return nil
    // }
    func testGet() {
        let url = "https://postman-echo.com/get"
        let query: NSDictionary = [
            "key1": "value1",
            "key2": "2"
        ]
        let promise = expectation(description: "Status code: 200")
        func success(response: NSObject!, urlResponse: HTTPURLResponse) {
            promise.fulfill()
        }
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            XCTFail("Error: \(error)")
        }
        dataManager.request(method: "GET", url: url, query: query, failure: failure, success: success)
        waitForExpectations(timeout: 10, handler: nil)
    }
    func testPost() {
        let url = "https://postman-echo.com/post"
        let body: NSDictionary = [
            "name": "post",
        ]
        let promise = expectation(description: "Status code: 200")
        func success(response: NSObject!, urlResponse: HTTPURLResponse) {
            promise.fulfill()
        }
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            XCTFail("Error: \(error)")
        }
        dataManager.request(method: "POST", url: url, body: body, failure: failure, success: success)
        waitForExpectations(timeout: 10, handler: nil)
    }
}

class UserSignupTests: XCTestCase {
    var dataManager: DataManager!
    var authManager: AuthenticationManager!
    override func setUp() {
        super.setUp()
        dataManager = DataManager()
        authManager = AuthenticationManager()
    }
    
    
    func testSignin() {
        let url = self.dataManager.config["baseUrl"]! + "api/authentication/verifyUserLoggedIn"
        let query: NSDictionary = [
            "access_token": "fra2",
        ]
        let promise = expectation(description: "Status code: 200")
        func success(response: NSObject!, urlResponse: HTTPURLResponse) {
            promise.fulfill()
        }
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            print("fuck fuck")
            XCTFail("Error: \(error)")
        }
        dataManager.request(method: "GET", url: url, query: query, failure: failure, success: success)
        waitForExpectations(timeout: 10, handler: nil)
    }
    
    
    func testSignup() {
        let url = self.dataManager.config["baseUrl"]! + "api/authentication/signup"
        let query: NSDictionary = [
            "username": "frankyang12244356"
        ]
        let promise = expectation(description: "Status code: 200")
        func success(response: NSObject!, httpRes: HTTPURLResponse) {
            let responseCode = httpRes.statusCode
            print("status received: ", responseCode)
            promise.fulfill()
        }
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            XCTFail("ErrorLALALALA: \(error)")
        }
        dataManager.request(method: "POST", url: url, query: query, failure: failure, success: success)
        waitForExpectations(timeout: 10, handler: nil)
    }
    
    func testSignInSuccess() {
        let promise = expectation(description: "Sign in success")
        authManager.writeStatus(status: "true")
        if authManager.checkStatus() {
            promise.fulfill()
        }
        waitForExpectations(timeout: 1, handler: nil)
    }
    
    func testSignInFail() {
        let promise = expectation(description: "Sign in fail")
        authManager.writeStatus(status: "false")
        if !authManager.checkStatus()  {
            promise.fulfill()
        }
        waitForExpectations(timeout: 1, handler: nil)
    }
    

}


class GroupManagerTests: XCTestCase {
    var dataManager: DataManager!
    var authManager: AuthenticationManager!
    var groupManager: GroupManager!
    override func setUp() {
        super.setUp()
        dataManager = DataManager()
        authManager = AuthenticationManager()
        groupManager = GroupManager()
    }
    
    func testCreateGroup() {
        let url = "http://localhost:8000/api/group/creategroup"
        let body: NSDictionary = [
            "name": "dinner",
            ]
        let query: NSDictionary = [
            "access_token": "frankyang",
            ]
        let promise = expectation(description: "Status code: 200")
        func success(response: NSObject!, httpRes: HTTPURLResponse) {
            let responseCode = httpRes.statusCode
            print("status received: ", responseCode)
            promise.fulfill()
        }
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            XCTFail("ErrorLALALALA: \(error)")
        }
        dataManager.request(method: "POST", url: url, query: query, body: body, failure: failure, success: success)
        waitForExpectations(timeout: 10, handler: nil)
    }
    
    func testGetGroupList() {
        let url = "http://localhost:8000/api/group/viewGroupOfUser"
        let query: NSDictionary = [
            "access_token": "frankyang",
            ]
        let promise = expectation(description: "Status code: 200")
        func success(response: NSObject!, httpRes: HTTPURLResponse) {
            let responseCode = httpRes.statusCode
            print("status received: ", responseCode)
            promise.fulfill()
        }
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            XCTFail("ErrorLALALALA: \(error)")
        }
        dataManager.request(method: "GET", url: url, query: query, failure: failure, success: success)
        waitForExpectations(timeout: 10, handler: nil)
    }
    
    func testGroupList() {
        let access_token = "frankyang"
        let promise = expectation(description: "Success")
        groupManager.getCurrentGroupList(withAccessToken: access_token) {(responseCode, groupList) in
            print("List: ", groupList)
            print("Code: ", responseCode)
            if (responseCode == 200) {
                promise.fulfill()
            }
        }
        waitForExpectations(timeout: 10, handler: nil)
    }
    
    func testGroupRemove() {
        let access_token = "frankyang"
        let promise = expectation(description: "Success")
        groupManager.leaveGroup(groupID: 1, withAccessToken: access_token) {(responseCode) in
            
            print("Code: ", responseCode)
            if (responseCode == 200) {
                promise.fulfill()
            }
        }
        waitForExpectations(timeout: 10, handler: nil)
    }
    
}

class PreferencesManagerTests: XCTestCase {
    var authenticationManager: AuthenticationManager!
    var preferencesManager: PreferencesManager!
    var userName: String = "username"
    override func setUp() {
        super.setUp()
        self.authenticationManager = AuthenticationManager()
        self.preferencesManager = PreferencesManager()
    }
    func testUpdatePreferences() {
        func failure(error: NSError!, httpRes: HTTPURLResponse) {
            XCTFail("Error: \(error)")
        }
        let promise = self.expectation(description: "Status code: 200")
        // Signup. If already signed up, does not matter if error
        self.authenticationManager.signup(userName: self.userName, password: "", email: "", completion: { (statusCode: Int) in
            // Get preferences
            self.preferencesManager.read(access_token: self.userName, failure: failure, success: {(response: NSObject?, urlResponse: HTTPURLResponse) in
                // Set dummy preferences
                let preferences: NSDictionary = [
                    "food_spicy": 0,
                    "food_vegan": 0,
                    "food_vegetarian": 0,
                    "place_loud": 0
                ]
                self.preferencesManager.update(access_token: self.userName, preferences: preferences, failure: failure, success: {(response: NSObject?, urlResponse: HTTPURLResponse) in
                    self.preferencesManager.read(access_token: self.userName, failure: failure, success: {(response: NSObject?, urlResponse: HTTPURLResponse) in
                        let responseMutable: NSMutableDictionary = NSMutableDictionary(dictionary: response as! NSDictionary)
                        responseMutable["id"] = nil
                        XCTAssertTrue(response === preferences)
                        promise.fulfill()
                    })
                })
            })
        })
        self.waitForExpectations(timeout: 10, handler: nil)
    }
}






















