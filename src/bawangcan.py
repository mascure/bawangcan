import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def process_category(url,driver):
    driver.get(url)
    try:
        #load all events
        while(1):
            time.sleep(8)
            more=driver.find_element_by_class_name("monad-more")
            more.click()
    except:
        print "no more!"
    elements=driver.find_elements_by_class_name("tit")
    all_event_url=[]
    for e in elements:
        a = e.find_element_by_tag_name("a")
        event_url= a.get_attribute("href")
        all_event_url.append(str(event_url))

        # start from your target element, here for example, "header"
        # all_children_by_css = header.find_elements_by_css_selector("*")
        # all_children_by_xpath = header.find_elements_by_xpath(".//*")
    total=all_event_url.__len__()
    print "start to process "+str(total)+" events.."
    cnt=0
    no=0
    for url in all_event_url:
        driver.get(url)
        no+=1
        try:
            big_btn=driver.find_element_by_class_name("big-btn")
            big_btn.click()
            time.sleep(1)
            ok=driver.find_element_by_id("J_pop_ok")
            ok.click()
            cnt+=1
            print str(no)+" success:"+driver.current_url
        except:
            print str(no)+' failed:'+driver.current_url
    print str(cnt)+' out of '+str(total)+' success!'
    return;

def main():
    print 'hello'

    print sys.argv
    print len(sys.argv)
    dper= sys.argv[1]
    #dper="a3769ff774628083846a7585e9beda09e3c7885bbde8410ed6c1a21bf3e8f2c3"
    print "your dper is:"+dper

    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=opts)
    #driver = webdriver.PhantomJS('/Users/mascure/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.maximize_window()

    driver.get("http://s.dianping.com/event/119124")
    driver.add_cookie({'name':'dper', 'value':dper,'path':'/'})
    category_urls=[]
    category_urls.append("http://s.dianping.com/event/shanghai/c1")
    category_urls.append("http://s.dianping.com/event/shanghai/c6")
    for url in category_urls:
        process_category(url, driver)
    driver.quit()


if __name__ == '__main__':
    main()
