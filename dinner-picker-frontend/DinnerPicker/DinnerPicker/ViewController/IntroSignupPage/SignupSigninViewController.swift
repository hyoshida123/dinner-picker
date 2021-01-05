//
//  SignupSigninViewController.swift
//  DinnerPicker
//
//  Created by Frank on 7/12/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class SignupSigninViewController: UIViewController {

    @IBOutlet weak var navigationBar: UINavigationItem!
    @IBOutlet weak var cancelButton: UIBarButtonItem!
    @IBOutlet weak var signInButton: UIButton!
    @IBOutlet weak var signUpButton: UIButton!
    @IBOutlet var nameEntryBox: UITextField!
    @IBOutlet var passwordEntryBox: UITextField!
    @IBOutlet var emptyUserNameText: UILabel!
    @IBOutlet var emptyPasswordText: UILabel!
    @IBOutlet var wrongPasswordText: UILabel!
    @IBOutlet var internetErrorText: UILabel!
    
    var authManager = AuthenticationManager()
    var dataManager = DataManager()
    
    override func viewDidLoad() {
        authManager = AuthenticationManager()
        dataManager = DataManager()
        emptyUserNameText.isHidden = true
        emptyPasswordText.isHidden = true
        wrongPasswordText.isHidden = true
        internetErrorText.isHidden = true
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func didCancelPress(_ sender: UIBarButtonItem) {
        self.dismiss(animated: true, completion: nil)
    }
    
    @IBAction func didSignInPress(_ sender: Any) {
        let userName: String = nameEntryBox.text!
        let password: String = passwordEntryBox.text!
        if !userName.isEmpty && !password.isEmpty {
            authManager.login(userName: userName, password: password) {
                (responseCode) in
                if responseCode == 200 {
                    self.displayDashboard()
                } else if responseCode == 0 {
                    self.internetErrorText.isHidden = false
                }
                else {
                    self.wrongPasswordText.isHidden = false
                }
            }
            
        } else if userName.isEmpty {
            emptyUserNameText.isHidden = false
        } else {
            emptyPasswordText.isHidden = false 
        }
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.emptyUserNameText.isHidden = true
            self.emptyPasswordText.isHidden = true
            self.wrongPasswordText.isHidden = true
            self.internetErrorText.isHidden = true
        }
    }
    
    func displayDashboard() {
        weak var presentingViewController = self.presentingViewController
        weak var rootVC = presentingViewController?.presentingViewController
        let dashboardVC = UIStoryboard(name: "Dashboard", bundle: nil).instantiateViewController(withIdentifier: "dashboard")
        self.dismiss(animated: true, completion: {presentingViewController?.dismiss(animated: true, completion: {rootVC?.present(dashboardVC, animated: false, completion: nil)})})
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
