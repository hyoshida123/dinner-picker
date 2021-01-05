//
//  IntroThirdViewController.swift
//  DinnerPicker
//
//  Created by Frank on 7/11/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class IntroThirdViewController: UIViewController {

    @IBOutlet weak var nextStepButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        nextStepButton.layer.cornerRadius = 10;
        nextStepButton.layer.borderWidth = 1;
        nextStepButton.layer.borderColor = UIColor.black.cgColor;

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    @IBOutlet weak var isNextStepPressed: UIButton!
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
