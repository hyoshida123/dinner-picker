//
//  SignUpInfoViewController.swift
//  DinnerPicker
//
//  Created by Frank on 7/19/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class SignUpInfoViewController: UIViewController {
    
    @IBOutlet var usernameEntryBox: UITextField!
    @IBOutlet var emailEntryBox: UITextField!
    @IBOutlet var passwordEntryBox: UITextField!
    @IBOutlet var confirmPWBox: UITextField!
    
    @IBOutlet var emptyUsernameText: UILabel!
    @IBOutlet var emptyPasswordText: UILabel!
    @IBOutlet var passwordNotMatchText: UILabel!
    @IBOutlet var usernameTakenTExt: UILabel!
    @IBOutlet var internetErrorText: UILabel!
    
    @IBOutlet weak var signMeUpButton: UIButton!
    
    var authManager = AuthenticationManager()
    var dataManager = DataManager()
    
    override func viewDidLoad() {
        authManager = AuthenticationManager()
        dataManager = DataManager()
        emptyPasswordText.isHidden = true
        emptyUsernameText.isHidden = true
        passwordNotMatchText.isHidden = true
        usernameTakenTExt.isHidden = true
        internetErrorText.isHidden = true
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    
    @IBAction func didSignMeUpPress(_ sender: Any) {
        let userName: String = usernameEntryBox.text!
        let email: String = emailEntryBox.text!
        let password: String = passwordEntryBox.text!
        let confirmPW: String = confirmPWBox.text!
        if userName.isEmpty {
            emptyUsernameText.isHidden = false
        } else if password.isEmpty {
            emptyPasswordText.isHidden = false
        } else if confirmPW.isEmpty {
            passwordNotMatchText.isHidden = false
        } else if password != confirmPW {
            passwordNotMatchText.isHidden = false
        } else {
            authManager.signup(userName: userName, password: password, email: email) {
                (responseCode) in
                if responseCode == 201 {
                    self.displayDashboard()
                } else if responseCode == 0 {
                    self.internetErrorText.isHidden = false
                }
                else {
                    self.usernameTakenTExt.isHidden = false
                }
            }
        }
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.emptyUsernameText.isHidden = true
            self.emptyPasswordText.isHidden = true
            self.passwordNotMatchText.isHidden = true
            self.passwordNotMatchText.isHidden = true
            self.usernameTakenTExt.isHidden = true
            self.internetErrorText.isHidden = true
        }
    
    }
    
    
    func displayDashboard() {
        weak var presentingViewController = self.presentingViewController
        weak var rootVC = presentingViewController?.presentingViewController
        let dashboardVC = UIStoryboard(name: "Dashboard", bundle: nil).instantiateViewController(withIdentifier: "dashboard")
        self.dismiss(animated: true, completion: {presentingViewController?.dismiss(animated: true, completion: {rootVC?.show(dashboardVC, sender: nil)})})
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        self.view.endEditing(true)
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
