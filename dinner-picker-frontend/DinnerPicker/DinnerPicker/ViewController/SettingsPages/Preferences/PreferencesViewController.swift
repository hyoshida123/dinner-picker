import UIKit

let PREFERENCE_OPTIONS = [
    "Must not have",
    "Strongly do not prefer",
    "Do not prefer",
    "Neutral",
    "Prefer",
    "Strongly prefer",
    "Must have"
]
let PREFERENCE_LABELS = [
    "food_spicy": [
        "title": "Spicy food",
        "description": "Do you prefer spicy food?"
    ],
    "food_vegan": [
        "title": "Vegan food",
        "description": "Do you prefer vegan food?"
    ],
    "food_vegetarian": [
        "title": "Vegetarian food",
        "description": "Do you prefer vegetarian food?"
    ],
    "place_loud": [
        "title": "Loud restaurants",
        "description": "Do you prefer eating in loud restaurants?"
    ]
]

class PreferencesViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet var signOutButton: UIBarButtonItem!
    
    
    @IBAction func didSavePress(_ sender: Any) {
        updatePreferences()
        print("preference saved")
        self.navigationController?.popViewController(animated: true)
    }
    
    override func viewDidLoad() {
        self.authenticationManager = AuthenticationManager()
        self.preferencesManager = PreferencesManager()
        self.token = authenticationManager.getToken()
        self.readPreferences()
        super.viewDidLoad()
        signOutButton = UIBarButtonItem.init(title: "Save", style: .done, target: self, action: #selector(PreferencesViewController.didSavePress))
        self.navigationItem.rightBarButtonItem = self.signOutButton
        
    }
    
    
    var authenticationManager = AuthenticationManager()
    var preferencesManager = PreferencesManager()
    var preferences: NSMutableDictionary = [:]
    var newPreferences: NSMutableDictionary = [:]
    var token: String!
    
    func failure(error: NSError, urlResponse: HTTPURLResponse) {
        
    }
    func updatePreferences() {
        var preferencesChanged = false
        for preferenceKey in preferences.allKeys {
            if preferences[preferenceKey as! String] as! Int != newPreferences[preferenceKey as! String] as! Int {
                preferencesChanged = true
                break
            }
        }
        if preferencesChanged {
            self.preferencesManager.update(access_token: self.token, preferences: self.newPreferences, failure: self.failure, success: {(response: NSObject?, urlResponse: HTTPURLResponse) in
                self.preferences = self.newPreferences.mutableCopy() as! NSMutableDictionary
            })
        }
    }
    func readPreferences() {
        self.preferencesManager.read(access_token: self.token, failure: self.failure, success: {(response: NSObject?, urlResponse: HTTPURLResponse) in
            let responseMutable: NSMutableDictionary = NSMutableDictionary(dictionary: response! as! NSDictionary)
            responseMutable["id"] = nil
            self.preferences = responseMutable.mutableCopy() as! NSMutableDictionary
            self.newPreferences = responseMutable.mutableCopy() as! NSMutableDictionary
            self.tableView.reloadData()
        })
    }
    
    // Table
    public func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return preferences.count
    }
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 240
    }
    public func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as! PreferenceTableViewCell
        let preferenceKey = self.preferences.allKeys[indexPath.row] as! String
        let preferenceSavedOption = self.preferences.allValues[indexPath.row] as! Int  //TODO: Error handling
        cell.preferenceTitle.text = PREFERENCE_LABELS[preferenceKey]?["title"]
        cell.preferenceDescription.text = PREFERENCE_LABELS[preferenceKey]?["description"]
        cell.preferenceKey = preferenceKey
        cell.newPreferences = self.newPreferences
        cell.pickerView.selectRow(preferenceSavedOption + 3, inComponent: 0, animated: false)
        return cell
    }
    // End Table
    
   
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}

















































