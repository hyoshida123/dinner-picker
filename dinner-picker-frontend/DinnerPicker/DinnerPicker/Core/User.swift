//
//  User.swift
//  DinnerPicker
//
//  Created by Frank on 8/10/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import Foundation

class User: NSObject {
    var userName: String
    var userToken: String
    var userEmail: String
    
    init(named: String, token: String, email: String) {
        userName = named
        userToken = token
        userEmail = email
    }
}
