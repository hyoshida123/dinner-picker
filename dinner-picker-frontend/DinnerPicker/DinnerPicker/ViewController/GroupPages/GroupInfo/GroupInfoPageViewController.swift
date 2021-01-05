//
//  GroupInfoPageViewController.swift
//  DinnerPicker
//
//  Created by Frank on 8/14/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit
import MapKit

class GroupInfoPageViewController: UIViewController {
    
    var groupName: String = ""
    var meetingLocation: String = ""
    var meetingTime: String = ""

    @IBOutlet var innerView: UIView!
    @IBOutlet var scrollView: UIScrollView!
    @IBOutlet var groupNameText: UILabel!
    @IBOutlet var meetingTimeText: UILabel!
    @IBOutlet var membersText: UILabel!
    @IBOutlet var locationText: UILabel!
    @IBOutlet var collectionView: UICollectionView!
    @IBOutlet var mapView: MKMapView!
    
    @IBOutlet var inviteButton: UIBarButtonItem!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.setGroupName()
        self.setLocation()
        self.setMeetingTime()
        // Do any additional setup after loading the view.
        
        inviteButton = UIBarButtonItem.init(title: "Invite", style: .done, target: self, action: #selector(GroupInfoPageViewController.didInvitePressed))
        self.navigationItem.rightBarButtonItem = self.inviteButton
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func setGroupName() {
        self.groupNameText.text = groupName
    }
    
    func setMeetingTime() {
        self.meetingTimeText.text = meetingTime
    }
    
    func setLocation() {
        self.locationText.text = meetingLocation
    }
    
    @IBAction func didInvitePressed(_ sender: Any) {
        
        print("Invite Pressed")
        
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
