//
//  GroupTableViewCell.swift
//  DinnerPicker
//
//  Created by Frank on 8/13/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class GroupTableViewCell: UITableViewCell {

    @IBOutlet var groupNameText: UILabel!
    @IBOutlet var meetingTimeText: UILabel!
    @IBOutlet var membersText: UILabel!
    @IBOutlet var locationText: UILabel!
    
    var parentViewController: UIViewController!
    

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }
    
    

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
        if selected {
            let groupInfoVC: GroupInfoPageViewController = UIStoryboard(name: "GroupInfoPage", bundle: nil).instantiateViewController(withIdentifier: "groupInfo") as! GroupInfoPageViewController
            groupInfoVC.groupName = self.groupNameText.text!
            groupInfoVC.meetingTime = self.meetingTimeText.text!
            groupInfoVC.meetingLocation = self.locationText.text!
            self.parentViewController.navigationController?.pushViewController(groupInfoVC, animated: true)
           
        }

        // Configure the view for the selected state
    }

}
