//
//  DashboardViewController.swift
//  DinnerPicker
//
//  Created by Frank on 7/19/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class DashboardViewController: UITabBarController {
    var prevVC: UIViewController!
    var authManager: AuthenticationManager!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        authManager = AuthenticationManager()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
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
