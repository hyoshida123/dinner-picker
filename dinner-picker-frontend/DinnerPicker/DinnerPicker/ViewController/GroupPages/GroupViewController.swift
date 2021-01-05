//
//  GroupTableViewController.swift
//  DinnerPicker
//
//  Created by Frank on 8/10/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class GroupViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    var groupManager = GroupManager.init()
    var authManager = AuthenticationManager()
    var access_token: String!
    var groupData: [Group] = []
    var refreshControl: UIRefreshControl!
    
    @IBOutlet var createButton: UIBarButtonItem!
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet var joinButton: UIBarButtonItem!
    
    
    
    
    override func viewWillAppear(_ animated: Bool) {
        self.refreshControl = getReloadObject()
        self.tableView.addSubview(self.refreshControl)
        groupManager = GroupManager.init()
        authManager = AuthenticationManager()
        
        access_token = authManager.getToken()
        self.navigationItem.rightBarButtonItem = self.createButton
        self.navigationItem.leftBarButtonItem = self.joinButton

        self.tableView.rowHeight = 160
        self.tableView.dataSource = self
        self.view.addSubview(self.tableView)
        self.refreshList()
    }
    
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
    }

    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return self.groupData.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 240
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as! GroupTableViewCell
        cell.accessoryType = .disclosureIndicator
        let group = groupData[indexPath.row]
        cell.groupNameText.text = group.getGroupName()
        cell.locationText.text = group.getLocation()
        cell.meetingTimeText.text = group.getTime()
        cell.membersText.text = group.getMembers()
        cell.parentViewController = self
        return cell
    }

    // MARK: - Table view data source

    @IBAction func isCreateGroupPressed(_ sender: Any) {
        let createGroupVC = UIStoryboard(name: "Dashboard", bundle: nil).instantiateViewController(withIdentifier: "createGroup") as! CreateGroupViewController
        createGroupVC.setGroupManager(groupMan: self.groupManager)
        self.navigationController?.pushViewController(createGroupVC, animated: true)
    }
    
    
    @IBAction func isJoinPressed(_ sender: Any) {
        print("joinButton!")
        let joinGroupVC = UIStoryboard(name: "JoinGroup", bundle: nil).instantiateViewController(withIdentifier: "joinGroup") as! JoinGroupViewController
        self.present(joinGroupVC, animated: true, completion: nil)
    }
    
    
    /**
     Handles refresh operations, updates the group list
     - parameter refreshControl: a refresh control instance
    */
    @objc private func handleRefresh(_ refreshControl: UIRefreshControl) {
        self.refreshList()
        refreshControl.endRefreshing()
    }
    
    /**
     Returns a UIRefreshControl Object that handles refresh operation
     - Returns: A UIRefreshControl object
     */
    private func getReloadObject() -> UIRefreshControl {
        let refreshControl = UIRefreshControl()
        refreshControl.addTarget(self, action:
            #selector(self.handleRefresh(_:)),
                                 for: UIControlEvents.valueChanged)
        refreshControl.tintColor = UIColor.red
        return refreshControl
    }
    
    /**
     Refreshes the current table cell list
     */
    private func refreshList() {
        self.groupManager.getCurrentGroupList(withAccessToken: access_token) {(responseCode, groupList) in
            if responseCode == 200 {
                self.groupData = groupList.sorted(by: {(group1: Group, group2: Group) -> Bool in return group1.groupName < group2.groupName})
                self.tableView.reloadData()
                print("Updated list")
            } else {
                print("update failed")
            }
            if self.groupData.count == 0 {
                self.tableView.isHidden = true
            } else {
                self.tableView.isHidden = false
            }
        }
    }
    
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            let group = self.groupData[indexPath.row]
            self.groupData.remove(at: indexPath.row)
            self.groupManager.leaveGroup(groupID: group.getID(), withAccessToken: access_token) {(responseCode) in
                //Do something?
            }
            tableView.deleteRows(at: [indexPath], with: .fade)
            
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }
    }
    
    
    
    
    


    /*
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    
    // Override to support editing the table view.


    /*
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
