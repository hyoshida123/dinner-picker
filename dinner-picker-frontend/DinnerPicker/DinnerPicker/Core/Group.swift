//
//  Group.swift
//  DinnerPicker
//
//  Created by Frank on 8/10/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import Foundation

class Group:NSObject {
    var groupID: Int
    var groupName: String
    var memberCount: Int
    var dateCreated: String
    var members: [User]
    var location: String
    
    init(id: Int, name: String, date: String, count: Int, location: String = "Somewhere") {
        self.groupID = id
        self.groupName = name
        self.memberCount = count
        self.dateCreated = date
        self.members = []
        self.location = location
    }
    
    func getGroupName() -> String {
        return self.groupName
    }
    
    func getID() -> Int {
        return self.groupID
    }
    
    func addUser(user: User) {
        self.members.append(user)
    }
    
    func getLocation() -> String {
        return self.location
    }
    
    func getTime() -> String {
        return self.dateCreated
    }
    
    func getMembers() -> String {
        return "No One"
    }
}
