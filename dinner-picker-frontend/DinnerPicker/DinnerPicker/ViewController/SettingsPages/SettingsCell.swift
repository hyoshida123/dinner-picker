//
//  SettingsCell.swift
//  DinnerPicker
//
//  Created by Frank on 8/14/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class SettingsCell: UITableViewCell {

    @IBOutlet var settingEntryText: UILabel!
    var parentViewController: UIViewController!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        if selected {
            let preferencesVC = UIStoryboard(name: "Preferences", bundle: nil).instantiateViewController(withIdentifier: "preferences")
        self.parentViewController.navigationController?.pushViewController(preferencesVC, animated: true)
        }
        // Configure the view for the selected state
        
    }

}
