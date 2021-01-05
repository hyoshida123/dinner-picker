//
//  SettingsViewController.swift
//  DinnerPicker
//
//  Created by Frank on 8/14/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class SettingsViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var authManager: AuthenticationManager!


    @IBOutlet var signOutButton: UIBarButtonItem!
    @IBOutlet var tableView: UITableView!
    
    override func viewWillAppear(_ animated: Bool) {
        self.tableView.dataSource = self
        self.view.addSubview(self.tableView)
        self.tableView.rowHeight = 60
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        authManager = AuthenticationManager()
        signOutButton = UIBarButtonItem.init(title: "Sign Out", style: .done, target: self, action: #selector(SettingsViewController.didSignOutPressed))
        self.navigationItem.rightBarButtonItem = self.signOutButton
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func didSignOutPressed(_ sender: Any) {
        let introPageVC = IntroPageViewController(transitionStyle: .scroll, navigationOrientation: .horizontal, options: nil)
        introPageVC.modalTransitionStyle = .flipHorizontal
        weak var presentingViewController = self.presentingViewController
        authManager.writeStatus(status: "false")
        authManager.saveToken(userToken: "")
        self.dismiss(animated: true, completion: {presentingViewController?.present(introPageVC, animated: true, completion: nil)})
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "settingCell", for: indexPath) as! SettingsCell
        cell.settingEntryText.text = "Preference"
        cell.accessoryType = .disclosureIndicator
        cell.parentViewController = self
        return cell
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
