import UIKit

class PreferenceTableViewCell: UITableViewCell, UIPickerViewDelegate, UIPickerViewDataSource {
    @IBOutlet weak var preferenceTitle: UILabel!
    @IBOutlet weak var preferenceDescription: UILabel!
    @IBOutlet weak var pickerView: UIPickerView!
    
    var newPreferences: NSMutableDictionary = [:]
    var preferenceKey: String? = nil
    
    // Picker
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return PREFERENCE_OPTIONS.count
    }
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return PREFERENCE_OPTIONS[row]
    }
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        self.newPreferences[preferenceKey!] = row - 3
    }
    // End Picker
    
    override func awakeFromNib() {
        super.awakeFromNib()
    }
    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
    }
}



















