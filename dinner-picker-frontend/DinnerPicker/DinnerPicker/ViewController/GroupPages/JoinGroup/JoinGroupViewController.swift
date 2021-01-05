//
//  JoinGroupViewController.swift
//  DinnerPicker
//
//  Created by Frank on 8/15/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class JoinGroupViewController: UIViewController {
    @IBOutlet var navigationBar: UINavigationBar!
    @IBOutlet var cancelButton: UIBarButtonItem!
    @IBOutlet var groupIDText: UILabel!
    @IBOutlet var idEntryBox: UITextField!
    @IBOutlet var joinButton: UIButton!
    @IBOutlet var topBar: UILabel!
    @IBOutlet var serverErrorText: UILabel!
    @IBOutlet var emptyIDText: UILabel!
    @IBOutlet var idDoesNotExistText: UILabel!
    
    var groupManager = GroupManager()
    var authManager = AuthenticationManager()
    
    override func viewWillAppear(_ animated: Bool) {
        self.groupManager = GroupManager()
        self.authManager = AuthenticationManager()
        self.serverErrorText.isHidden = true
        self.emptyIDText.isHidden = true
        self.idDoesNotExistText.isHidden = true
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    @IBAction func didCancelPressed(_ sender: Any) {
        self.dismiss(animated: true, completion: nil)
    }
    
    @IBAction func didJoinPressed(_ sender: Any) {
        let groupID: String = self.idEntryBox.text!
        if !groupID.isEmpty {
            self.groupManager.joinGroup(groupID: Int(groupID)!, withAccessToken: authManager.getToken()) {(responseCode) in
                if (responseCode == 200) {
                    self.dismiss(animated: true, completion: nil)
                } else if responseCode == 400 {
                    self.idDoesNotExistText.isHidden = false
                } else {
                    self.serverErrorText.isHidden = false
                }
            }
        } else {
            self.emptyIDText.isHidden = false
        }
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.serverErrorText.isHidden = true
            self.emptyIDText.isHidden = true
            self.idDoesNotExistText.isHidden = true
        }
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
