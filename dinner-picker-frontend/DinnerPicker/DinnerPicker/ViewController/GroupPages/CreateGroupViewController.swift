//
//  CreateGroupViewController.swift
//  DinnerPicker
//
//  Created by Frank on 8/10/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class CreateGroupViewController: UIViewController {

    @IBOutlet var groupNameLabelText: UILabel!
    @IBOutlet var groupNameEntryBox: UITextField!
    @IBOutlet var datePicker: UIDatePicker!
    @IBOutlet var meetingTimeLabel: UILabel!
    @IBOutlet var createGroupButton: UIButton!
    @IBOutlet var emptyNameText: UILabel!
    
    var authManager = AuthenticationManager()
    var dataManager = DataManager()
    var groupManager: GroupManager? = nil
    
    override func viewDidLoad() {
        super.viewDidLoad()
        authManager = AuthenticationManager()
        dataManager = DataManager()
        groupManager = GroupManager.init()
        createGroupButton.layer.cornerRadius = 5;
        createGroupButton.layer.borderWidth = 1;
        createGroupButton.layer.borderColor = UIColor.black.cgColor;
        emptyNameText.isHidden = true
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func isCreateGroupButtonPressed(_ sender: Any) {
        let groupName: String = groupNameEntryBox.text!
        if (groupName.isEmpty) {
            self.emptyNameText.isHidden = false
        } else {
            let accessToken: String = authManager.getToken()
            groupManager?.createGroup(groupName: groupName, withAccessToken: accessToken) {(responseCode, group) in
                print("response Code", responseCode)
                if (responseCode == 200) {
                    print(group) // TODO: Do something with the group
                    self.navigationController?.popViewController(animated: true)
                } else {
                    print("create failure, try again")
                }
            }
        }
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.emptyNameText.isHidden = true
        }
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        self.view.endEditing(true)
    }
    
    func setGroupManager(groupMan: GroupManager) {
        print("groupManager set")
        self.groupManager = groupMan
    }
    
    
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
