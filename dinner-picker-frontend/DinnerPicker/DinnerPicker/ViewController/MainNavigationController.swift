//
//  MainNavigationController.swift
//  DinnerPicker
//
//  Created by Frank on 7/27/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class MainNavigationController: UIViewController {
    var authManager: AuthenticationManager!

    override func viewDidLoad() {
        super.viewDidLoad()
        authManager = AuthenticationManager()
        view.backgroundColor = .white
        print("Status: ", authManager.checkStatus())
        if !authManager.checkStatus() {
            perform(#selector(showIntroPageVC), with: nil, afterDelay: 0.1)
            //perform(#selector(showDashboardVC), with: nil, afterDelay: 1)
        } else {
            perform(#selector(showDashboardVC), with: nil, afterDelay: 0.1)
        }
        // Do any additional setup after loading the view.
    }
    
    @objc func showIntroPageVC() {
        let introPageVC = IntroPageViewController(transitionStyle: .scroll, navigationOrientation: .horizontal, options: nil)
        present(introPageVC, animated: true, completion: nil)
    }
    
    @objc func showDashboardVC() {
        let dashboardVC = UIStoryboard(name: "Dashboard", bundle: nil).instantiateViewController(withIdentifier: "dashboard")
        self.present(dashboardVC, animated: false, completion: nil)
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
