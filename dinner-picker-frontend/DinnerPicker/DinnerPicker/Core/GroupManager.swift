//
//  GroupManager.swift
//  DinnerPicker
//
//  Created by Frank on 8/10/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import Foundation
class GroupManager: NSObject {
    let createGroupURL = "http://localhost:8000/api/group/creategroup"
    let joinGroupURL = "http://localhost:8000/api/group/joingroup"
    let listCurrentGroupURL = "http://localhost:8000/api/group/viewGroupOfUser"
    let leaveGroupURL = "http://localhost:8000/api/group/leavegroup"
    let listGroupHistoryURL = "http://localhost:8000/api/group/listAllGroups"
    let groupListUserURL = "http://localhost:8000/api/group/list_users_in_group"
    
    var groupList: [Group]  // A list that stores all groups that are active
    var dataManager: DataManager!
    
    override init() {
        self.groupList = []
        self.dataManager = DataManager()
    }
    
    /**
     Create a new Group
     - parameter groupName: The name of the newly created group
     - parameter withAccessToken: the access token of the current user
     - parameter completion: call back function that takes in a status code
     - parameter statusCode: status code that is returned from HTTPResponse
     */
    func createGroup(groupName: String, withAccessToken: String, completion: @escaping (_ statusCode: Int, _ group: Group) ->  ()) {
        let loginQuery: NSDictionary = ["access_token": withAccessToken]
        let bodyData: NSDictionary = ["name": groupName]
        self.dataManager.request(method: "POST", url: createGroupURL, query: loginQuery, body: bodyData,
                                 failure: {(error: NSError!, urlResponse: HTTPURLResponse) in
                                    completion(urlResponse.statusCode, Group(id: -99, name: "", date: "", count: 0))
                                            print("Create Failure")},
                                 success: {(response: NSObject!, urlResponse: HTTPURLResponse) in
                                            if urlResponse.statusCode == 200 {
                                                print("Create success")
                                                let newGroup: Group = self.createGroupInstanceWithJSON(received: response)
                                                completion(urlResponse.statusCode, newGroup)
                                                self.groupList.append(newGroup)
                                            } else {
                                                print("Create failure")}})
    }
    
    /**
     Leaves the current group
     - parameter groupID: the id of the group that the user wants to leave from
     - parameter withAccessToken: the access token of the current user
     - parameter completion: call back function that takes in a status code
     - parameter statusCode: status code that is returned from HTTPResponse
     */
    func leaveGroup(groupID: Int, withAccessToken: String, completion: @escaping (_ statusCode: Int) ->  ()) {
        let loginQuery: NSDictionary = ["access_token": withAccessToken]
        let bodyData: NSDictionary = ["id": String(groupID)]
        self.dataManager.request(method: "DELETE", url: leaveGroupURL, query: loginQuery, body: bodyData,
                                 failure: {(error: NSError!, urlResponse: HTTPURLResponse) in
                                    completion(urlResponse.statusCode)
                                    print("Leave Failure", error)},
                                 success: {(response: NSObject!, urlResponse: HTTPURLResponse) in
                                    if urlResponse.statusCode == 200 {
                                        print("Leave success")
                                        completion(urlResponse.statusCode)
                                    } else {
                                        print(response)
                                        print("Leave failure")}})
    }
    
    
    /**
     Joins a group using currect access_token
     - parameter groupID: the id of the group that the user wants to leave from
     - parameter withAccessToken: the access token of the current user
     - parameter completion: call back function that takes in a status code
     - parameter statusCode: status code that is returned from HTTPResponse
     */
    func joinGroup(groupID: Int, withAccessToken: String, completion: @escaping (_ statusCode: Int) ->  ()) {
        let loginQuery: NSDictionary = ["access_token": withAccessToken]
        let bodyData: NSDictionary = ["id":String(groupID)]
        self.dataManager.request(method: "POST", url: joinGroupURL, query: loginQuery, body: bodyData,
                                 failure: {(error: NSError!, urlResponse: HTTPURLResponse) in
                                    completion(urlResponse.statusCode)
                                    print("Join Failure")},
                                 success: {(response: NSObject!, urlResponse: HTTPURLResponse) in
                                    if urlResponse.statusCode == 200 {
                                        print("Join success")
                                        //let newGroup: Group = self.createGroupInstanceWithJSON(received: response)
                                        //self.groupList.append(newGroup)
                                        completion(urlResponse.statusCode)
                                    } else {
                                        completion(urlResponse.statusCode)
                                        print("Join failure")}})
    }
    
    /**
     Access the information of all the groups that the user is currently in
     - parameter withAccessToken: access token of current user
     - parameter completion: callback function
     - parameter statusCode: status code received by HTTPResponse
     - parameter groupList: a list containing all group information
     **/
    func getCurrentGroupList(withAccessToken: String, completion: @escaping (_ statusCode: Int, _ groupList: [Group]) ->  ()) {
        let loginQuery: NSDictionary = ["access_token": withAccessToken]
        self.dataManager.request(method: "GET", url: listCurrentGroupURL, query: loginQuery,
                                 failure: {(error: NSError!, urlResponse: HTTPURLResponse) in
                                    completion(urlResponse.statusCode, [])
                                    print("Create Failure")},
                                 success: {(response: NSObject!, urlResponse: HTTPURLResponse) in
                                    if urlResponse.statusCode == 200 {
                                        print("Create success")
                                        let list: NSArray = response as! NSArray // request is an array of dicts
                                        var finalList: [Group] = []
                                        for groupInfo in list {
                                            let group = self.createGroupInstanceWithJSON(received: groupInfo as! NSObject)
                                            self.groupList.append(group)
                                            finalList.append(group)
                                        }
                                        completion(urlResponse.statusCode, finalList)
                                    } else {
                                        print("Create failure")}})
    }
    
    /**
     Returns a Group instance using the received JSON object
     - parameter received: an NSDictionary containing group information
    */
    func createGroupInstanceWithJSON(received: NSObject) -> Group {
        return Group(id: (received as! NSDictionary)["id"] as! Int,
                     name: (received as! NSDictionary)["name"] as! String,
                     date: (received as! NSDictionary)["created"] as! String,
                     count: 1)
    }
}
