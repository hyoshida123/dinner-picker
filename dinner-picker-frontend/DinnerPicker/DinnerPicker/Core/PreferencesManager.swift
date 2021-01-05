import UIKit

class PreferencesManager: NSObject {
    var dataManager: DataManager = DataManager()
    var url: String!
    override init() {
        super.init()
        self.dataManager = DataManager()
        self.url = dataManager.config["baseUrl"]! + "api/settings/preference"
    }
    func read(access_token: String!, failure: @escaping (_ error: NSError, _ urlResponse: HTTPURLResponse) -> (), success: @escaping (_ response: NSObject, _ urlResponse: HTTPURLResponse) -> ()) {
        let query: NSDictionary = [
            "access_token": access_token
        ]
        self.dataManager.request(method: "GET", url: self.url, query: query, failure: failure, success: success)
    }
    func update(access_token: String!, preferences: NSDictionary!, failure: @escaping (_ error: NSError, _ urlResponse: HTTPURLResponse) -> (), success: @escaping (_ response: NSObject, _ urlResponse: HTTPURLResponse) -> ()) {
        let query: NSDictionary = [
            "access_token": access_token
        ]
        var preferencesAsStringStringPair: [String:String] = [:]
        for preferenceKey in preferences.allKeys {
            preferencesAsStringStringPair[preferenceKey as! String] = "\(preferences[preferenceKey]!)"
        }
        self.dataManager.request(method: "POST", url: self.url, query: query, body: preferencesAsStringStringPair as NSDictionary, failure: failure, success: success)
    }
}
