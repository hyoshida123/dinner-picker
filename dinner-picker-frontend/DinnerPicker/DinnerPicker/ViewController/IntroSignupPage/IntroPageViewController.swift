//
//  IntroPageViewController.swift
//  DinnerPicker
//
//  Created by Frank on 7/8/18.
//  Copyright © 2018 Guowei Yang. All rights reserved.
//

import UIKit

class IntroPageViewController: UIPageViewController, UIPageViewControllerDelegate, UIPageViewControllerDataSource {
    
    
    lazy var VCArr: [UIViewController] = {
        return [self.VCInstance(name: "firstIntro"),
                self.VCInstance(name: "secondIntro"),
                self.VCInstance(name: "thirdIntro"),
                self.VCInstance(name: "fourthIntro")]
    } ()
    
    /** Create ViewController Instances*/
    func VCInstance(name: String) -> UIViewController {
        return UIStoryboard(name: "IntroPageView", bundle: nil).instantiateViewController(withIdentifier: name)
    }
    
    /** Takes care of scrolling to the right (previous page) */
    func pageViewController(_ pageViewController: UIPageViewController, viewControllerBefore viewController: UIViewController) -> UIViewController? {
        guard let viewControllerIndex = VCArr.index(of: viewController) else {
            return nil
        }
        let previousIndex = viewControllerIndex - 1
        
        guard previousIndex >= 0 else {
            return VCArr.last
        }
        
        guard VCArr.count > previousIndex else {
            return nil //Avoid crash when out of bounds
        }
        return VCArr[previousIndex]
    }
    
    /** Take care of scrolling to the left (next page) */
    func pageViewController(_ pageViewController: UIPageViewController, viewControllerAfter viewController: UIViewController) -> UIViewController? {
        guard let viewControllerIndex = VCArr.index(of: viewController) else {
            return nil
        }
        let nextIndex = viewControllerIndex + 1
        
        guard nextIndex < VCArr.count else {
            return VCArr.first
        }
        
        guard VCArr.count > nextIndex else {
            return nil //Avoid crash when out of bounds
        }
        return VCArr[nextIndex]
    }
    
    /** Returns the total amount of ViewControllers*/
    func presentationCount(for pageViewController: UIPageViewController) -> Int {
        return VCArr.count
    }
    
    /** Returns the index of the current ViewController*/
    func presentationIndex(for pageViewController: UIPageViewController) -> Int {
        guard let firstViewController = viewControllers?.first,
              let firstViewControllerIndex = VCArr.index(of: firstViewController) else {
            return 0
        }
        return firstViewControllerIndex
    }
    
    /** Overrides the default constructor and sets the transition style to scroll*/
    override init(transitionStyle style:
        UIPageViewControllerTransitionStyle, navigationOrientation: UIPageViewControllerNavigationOrientation, options: [String : Any]? = nil) {
        super.init(transitionStyle: .scroll, navigationOrientation: .horizontal, options: [UIPageViewControllerOptionInterPageSpacingKey: 4])
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.dataSource = self
        self.delegate = self
        if let firstIntro = VCArr.first{
            self.setViewControllers([firstIntro], direction: .forward, animated: true, completion: nil)
        }
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func selfDismiss() {
        self.dismiss(animated: true, completion: nil)
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
