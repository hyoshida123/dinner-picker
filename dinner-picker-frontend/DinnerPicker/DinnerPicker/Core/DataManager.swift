import Foundation

func getConfig() -> [String: String] {
    let path = Bundle.main.path(forResource: "Config", ofType: "plist")
    return NSDictionary(contentsOfFile: path!) as! [String: String]
}

class DataManager: NSObject {
    var config: [String: String]!
    override init() {
        super.init()
        self.config = getConfig()
    }
    func request(method: String!, url: String!, query: NSDictionary? = nil, body: NSDictionary? = nil,
                 failure: @escaping (_ error: NSError, _ urlResponse: HTTPURLResponse) -> (),
                 success: @escaping (_ response: NSObject, _ urlResponse: HTTPURLResponse) -> ()) {
        var components = URLComponents(string: url)!
        if query != nil {
            components.queryItems = (query as! [String: String]).map {
                return URLQueryItem(name: $0, value: $1)
            }
        }
        let request: NSMutableURLRequest = NSMutableURLRequest(url: NSURL(string: (components.url?.absoluteString)!)! as URL)
        request.httpMethod = method
        if body != nil {
            request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
            request.setValue("application/json", forHTTPHeaderField: "Accept")
            let bodyData: String = convertToParameters((body as! [String: String?]))
            request.httpBody = bodyData.data(using: String.Encoding.utf8)
            
        }
        let session = URLSession.shared
//        let task = session.dataTask(with: request as URLRequest) {(data, response, error) in
        NSURLConnection.sendAsynchronousRequest(request as URLRequest, queue: OperationQueue.main) {(response, data, error) in
            if error != nil {
                var httpResponse = response as? HTTPURLResponse
                if httpResponse != nil {
                    failure(error! as NSError, httpResponse!)
                } else if error!._code == -1012{
                    httpResponse = HTTPURLResponse(url: NSURL(string: (components.url?.absoluteString)!)! as URL, statusCode: 401, httpVersion: nil, headerFields: nil)
                    failure(error! as NSError, httpResponse!)
                }
                else {
                    httpResponse = HTTPURLResponse()
                    failure(error! as NSError, httpResponse!)
                }
            }
            else {
                let httpResponse = response as? HTTPURLResponse
                if data != nil {
                    let dataAsString = String(data: data!, encoding: String.Encoding(rawValue: String.Encoding.utf8.rawValue))!
                    let dataAsData = dataAsString.data(using: .utf8)
                    do {
                        success((try JSONSerialization.jsonObject(with: dataAsData!, options: .allowFragments) as! NSObject), httpResponse!)
                    }
                    catch {
                        failure(NSError(domain: "Non-JSON response:" + dataAsString, code: -1), httpResponse!)
                    }
                }
                else {
                    failure(NSError(domain: "Data is nil", code: -1), httpResponse!)
                }
            }
        }
        //task.resume()
    }
    
    func convertToParameters(_ params: [String: String?]) -> String {
        var paramList: [String] = []
        
        for (key, value) in params {
            guard let value = value else {
                continue
            }
            guard let scapedKey = key.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed) else {
                print("Failed to convert key \(key)")
                continue
            }
            guard let scapedValue = value.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed) else {
                print("Failed to convert value \(value)")
                continue
            }
            paramList.append("\(scapedKey)=\(scapedValue)")
        }
        return paramList.joined(separator: "&")
    }
}



































