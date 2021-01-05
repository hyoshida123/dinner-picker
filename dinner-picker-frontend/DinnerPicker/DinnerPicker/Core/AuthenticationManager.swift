//
//  AuthenticationManager.swift
//  DinnerPicker
//
//  Created by Frank on 7/29/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import Foundation
//global url
class AuthenticationManager: NSObject {
    let signupURL = "http://localhost:8000/api/authentication/signup"
    let signinURL = "http://localhost:8000/api/authentication/verifyUserLoggedIn"
    var requestFulfilled = false
    var statusCode = 404
    let tokenFile = "access.token"
    let statusFile = "signin.status"
    
    
    var dataManager: DataManager = DataManager() 
    
    func AuthenticationManager() {
        self.dataManager = DataManager()
    }
    
    /** Log-in method */
    func login(userName: String, password: String, completion: @escaping (_ statusCode: Int) ->  ()) {
        let loginQuery: NSDictionary = [
            "access_token": userName
        ]
        self.dataManager.request(method: "GET", url: self.signinURL, query: loginQuery,
                                failure: {(error: NSError!, urlResponse: HTTPURLResponse) in
                                            completion(urlResponse.statusCode)
                                            print("Sign-in Failure")
                                            self.writeStatus(status: "false")},
                                success: {(response: NSObject!, urlResponse: HTTPURLResponse) in
                                            completion(urlResponse.statusCode)
                                            if urlResponse.statusCode == 200 {
                                                self.writeStatus(status: "true")
                                                self.saveToken(userToken: userName)
                                            } else {
                                                self.writeStatus(status: "false")}})
    }
    
    
    func signup(userName: String, password: String, email: String, completion: @escaping (_ statusCode: Int) ->  ()) {
        let loginQuery: NSDictionary = [
            "username": userName
        ]
        self.dataManager.request(method: "POST", url: self.signupURL, query: loginQuery,
                                 failure: {(error: NSError!, urlResponse: HTTPURLResponse) in
                                    completion(urlResponse.statusCode)
                                    print("Sign-in Failure")
                                    self.writeStatus(status: "fail")},
                                 success: {(response: NSObject!, urlResponse: HTTPURLResponse) in
                                    completion(urlResponse.statusCode)
                                    if urlResponse.statusCode == 200 {
                                        self.writeStatus(status: "true")
                                    } else {
                                        self.writeStatus(status: "false")
                                    }
                                    self.saveToken(userToken: (response as! NSDictionary)["name"] as! String)
                                })
        }
    
    
    func isSignedIn() -> Bool {
        return checkStatus()
    }
    
    /** Write sign in status to file*/
    func writeStatus(status: String) {
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            let fileURL = dir.appendingPathComponent(statusFile)
            do {
                try status.write(to: fileURL, atomically: false, encoding: .utf8)
            }
            catch {
                print("Write Failed.")
            }
        }
    }
    
    /** Checks status of the current user. */
    func checkStatus() -> Bool {
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            do {
                let fileURL = dir.appendingPathComponent(statusFile)
                let text2 = try String(contentsOf: fileURL, encoding: .utf8)
                if (text2 == "true") {
                    return true  //TODO: Change back
                } else {
                    return false
                }
            }
            catch {
                print("read failed")
            }
        }
        return false
    }
    
    func saveToken(userToken: String) {
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            let fileURL = dir.appendingPathComponent(tokenFile)
            do {
                try userToken.write(to: fileURL, atomically: false, encoding: .utf8)
            }
            catch {
                print("Write Failed.")
            }
        }
    }
    
    func getToken() -> String {
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            do {
                let fileURL = dir.appendingPathComponent(tokenFile)
                let text = try String(contentsOf: fileURL, encoding: .utf8)
                return text
            }
            catch {
                print("read failed")
            }
        }
        return ""
    }
}

