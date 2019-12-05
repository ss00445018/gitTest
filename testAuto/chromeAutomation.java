package testAuto;

import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;

import javax.net.ssl.HttpsURLConnection;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.NoAlertPresentException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.logging.LogEntries;
import org.openqa.selenium.logging.LogEntry;
import org.openqa.selenium.logging.LogType;
import org.openqa.selenium.logging.LoggingPreferences;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.SessionId;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class chromeAutomation {
	private WebDriver driver = null;
	
	public static void main(String[] args) throws Exception {

		String processName = "chrome.exe";
		String chromeDriver = "chromedriver.exe";
		String TASKLIST = "tasklist";
		Process p = Runtime.getRuntime().exec(TASKLIST);
		BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
		String line;
		while ((line = reader.readLine()) != null) {
			 if (line.contains(processName)) {
				Runtime.getRuntime().exec("taskkill /F /IM " + processName);
			}
			if (line.contains(chromeDriver)) {
				Runtime.getRuntime().exec("taskkill /F /IM " + chromeDriver);
			}
		} 

		Thread.sleep(2000);
		File chrome = new File("C:\\ProgramData\\IAF\\bin\\webdrivers\\chromedriver.exe");
		System.setProperty("webdriver.chrome.driver", chrome.getAbsolutePath());
		
		// ChromeOptions options = new ChromeOptions();
		Map<String, Object> chromeOptions = new HashMap<String, Object>();

		DesiredCapabilities capabilities = DesiredCapabilities.chrome();
		capabilities.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
		capabilities.setCapability(CapabilityType.SUPPORTS_WEB_STORAGE, true);
		capabilities.setCapability(CapabilityType.HAS_NATIVE_EVENTS, true);
		capabilities.setCapability(CapabilityType.SUPPORTS_APPLICATION_CACHE, true);
		capabilities.setCapability(CapabilityType.SUPPORTS_JAVASCRIPT, true);
		
		Map<String, String> mobileEmulation = new HashMap<>();
		mobileEmulation.put("deviceName", "iPhone 6/7/8 Plus");
		// chromeOptions.put("mobileEmulation", mobileEmulation);
		chromeOptions.put("useAutomationExtension", false);
		LoggingPreferences preferences = new LoggingPreferences();
		preferences.enable(LogType.PERFORMANCE, Level.ALL);
		capabilities.setCapability(CapabilityType.LOGGING_PREFS, preferences);
		capabilities.setCapability( "goog:loggingPrefs", preferences ); 
		
		if (chromeOptions.size() > 0) {
			capabilities.setCapability(ChromeOptions.CAPABILITY, chromeOptions);
		}
		
		WebDriver driver = new ChromeDriver(capabilities);
		String appUrl = "https://zlt16161.vci.att.com:32201";
		driver.get(appUrl);
		System.out.println(driver.getTitle());
		driver.manage().window().maximize();

		driver.findElement(By.xpath("//input[@id=\"GloATTUID\"]")).sendKeys("aa716q");
		driver.findElement(By.xpath("//input[@id=\"GloPassword\"]")).sendKeys("123123a");
		Thread.sleep(1000);
		driver.findElement(By.xpath("//input[@id=\"GloPasswordSubmit\"]")).click();
		Thread.sleep(1000);
		driver.findElement(By.xpath("//input[@id=\"successButtonId\"]")).click();
		Thread.sleep(4000);
		driver.findElement(By.xpath("//div[@id=\"time\"]")).click();
		
		Thread.sleep(1000);
		
		// chooseBsDateFromPicker(driver);
		System.out.println("Done");
		
		OutputStream logfile = new FileOutputStream(new File("C:\\sx5780\\Programs\\Workspace\\temp\\" + new Date().toString().replaceAll(" ", "_").replaceAll(":", "_") + ".txt"),true);
		PrintStream printlog = new PrintStream(logfile);
        LogEntries logs = driver.manage().logs().get(LogType.PERFORMANCE);
        for (LogEntry entry : logs) {
             // if(entry.toString().contains("\"type\":\"XHR\"")) {

                printlog.append(new Date(entry.getTimestamp()) + " " + entry.toString() +" "+ System.getProperty("line.separator"));
                printlog.append(System.getProperty("line.separator"));
                printlog.append(System.getProperty("line.separator"));
            // }
        }
        printlog.close();
	}
	
	private static String monthInt2Str(int reqMonth) {
		switch (reqMonth) {
			case 1:
				return "Jan";
			case 2:
				return "Feb";
			case 3:
				return "Mar";
			case 4:
				return "Apr";
			case 5:
				return "May";
			case 6:
				return "Jun";
			case 7:
				return "Jul";
			case 8:
				return "Aug";
			case 9:
				return "Sep";
			case 10:
				return "Oct";
			case 11:
				return "Nov";
			case 12:
				return "Dec";
			default:
				return "";
		}
	}
	
	private static void chooseBsDateFromPicker(WebDriver driver) {
		String reqDateStr = "11/01/2018";
		String dateFormat = "MM/DD/YYYY";
		
		int reqMonth = 0;
		int reqDay = 0;
		int reqYear = 0;
		switch (dateFormat.toUpperCase()) {
			case "MM/DD/YYYY":
				try {
					reqMonth = Integer.parseInt(reqDateStr.substring(0, 2));
					reqDay = Integer.parseInt(reqDateStr.substring(3, 5));
					reqYear = Integer.parseInt(reqDateStr.substring(6, 10));
				} catch (Exception e) {
					return;					
				}
				break;
				
			default:
				return;				
		}
		
		String reqMonthStr = monthInt2Str(reqMonth);
		if (reqMonthStr.length() == 0) {
			return;
		}
		
		int curYear = Calendar.getInstance().get(Calendar.YEAR);
		int switchClicks = curYear - reqYear;
		/* steps
		 * 	1. Keep Clicking header till year is displayed
		 * 	2. click on required year
		 * 	3. click on required month
		 * 	4. click on required day
		*/
		try {
			String orgXpath = "//div[@class=\"bs-calendar-container\"]";
			String tmpXpath = "";
			
			tmpXpath = (orgXpath + "//button[@class='current']");
			WebElement element = driver.findElement(By.xpath(tmpXpath));
			if (element == null) {
				return;
			}
			scrollIntoView(driver, element);
			element.click();
			Thread.sleep(1000);
			//click prev or next based on switchClicks
			if (switchClicks != 0) {
				if (switchClicks < 0) {
					// next
					tmpXpath = orgXpath + "//button[@class='next']";
					switchClicks = switchClicks * -1;
				} else {
					// prev
					tmpXpath = orgXpath + "//button[@class='previous']";
				}
				element = driver.findElement(By.xpath(tmpXpath));
				if (element == null) {
					return;
				}
				for(int i = 0; i < switchClicks; i++) {					
					element.click();
					Thread.sleep(100);
				}				
			}
			
			// click on Month
			tmpXpath = orgXpath+ "//table[@class='months']//span";
			element = null;
			List<WebElement> allSpans = driver.findElements(By.xpath(tmpXpath));
			for(WebElement ele: allSpans) {
				String innerHtml = ele.getAttribute("innerHTML");
				if (innerHtml.contains(reqMonthStr)) {
					element = ele;
					break;
				}
			}
			
			if (element == null) {
				return;
			}
			element.click();
			Thread.sleep(100);
			
			// click on day
			
			tmpXpath = orgXpath + "//table[@class='days weeks']//span[not(@class='is-other-month') and text()='" + reqDay + "']";
			element = driver.findElement(By.xpath(tmpXpath));
			if (element == null) {
				return;
			}
			
			element.click();
			Thread.sleep(100);
			
		} catch (Exception e) {
			return;
		}
	}
	
	protected static void scrollIntoView(WebDriver driver, WebElement element) {
		if (!element.isDisplayed()) {
			((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView();",element);			
		}
	}
}
