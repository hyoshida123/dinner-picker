//
//  InntroFirstPageViewController.swift
//  DinnerPicker
//
//  Created by Frank on 7/9/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class IntroFirstViewController: UIViewController {


    @IBOutlet weak var foodImageView: UIImageView!
    @IBOutlet weak var nextStepButton: UIButton!
    @IBOutlet weak var backgroundFoodImage: UIImageView!
    @IBOutlet weak var backgroundBlur: UIVisualEffectView!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        super.viewDidLoad()
        nextStepButton.layer.cornerRadius = 10;
        nextStepButton.layer.borderWidth = 1;
        nextStepButton.layer.borderColor = UIColor.black.cgColor;
        
        backgroundFoodImage.layer.cornerRadius = 10;

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    @IBAction func didNextStepPressed(_ sender: Any) {
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
