package allSeleniumMethods;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class AllJavaScriptExecuter {

	public static void main(String[] args) {
		ChromeDriver driver = new ChromeDriver();
		JavascriptExecutor js=(JavascriptExecutor)driver;
		WebElement e=driver.findElement(By.xpath(""));
		

//		Clicking an Element (Bypassing Selenium click issues)
		WebElement button = driver.findElement(By.id("submitBtn"));
		js.executeScript("arguments[0].click();", button);
		
//		 Scroll Down / Up
//		Scroll down to the bottom:
		js.executeScript("window.scrollTo(0, document.body.scrollHeight);");
//		Scroll to specific pixel:
		js.executeScript("window.scrollBy(0, 500);"); // Scroll down 500px
//		Scroll to an element:
		WebElement element = driver.findElement(By.id("footer"));
		js.executeScript("arguments[0].scrollIntoView(true);", element);
		
//		 Send Keys / Set Value in Input Field
		WebElement inputField = driver.findElement(By.id("username"));
		js.executeScript("arguments[0].value='bhupi';", inputField);
		
//		Get Page Title Using JavaScript
		String title = (String) js.executeScript("return document.title;");
		System.out.println("Page Title is: " + title);
		
//		Get URL of Current Page
		String url = (String) js.executeScript("return document.URL;");
		System.out.println("URL is: " + url);

//		Highlight an Element (For debugging, demos, or just drama)
		WebElement elem = driver.findElement(By.id("highlightMe"));
		js.executeScript("arguments[0].style.border='3px solid red'", elem);

//		Refresh the Page
		js.executeScript("history.go(0);");

//		Get InnerText of the Whole Page
		String pageText = (String) js.executeScript("return document.documentElement.innerText;");
		System.out.println(pageText);

//		Disable an Input Field (Why? Because you can!)
		js.executeScript("document.getElementById('email').disabled=true;");

//		Check if Page is Fully Loaded
		String state = (String) js.executeScript("return document.readyState;");
		if (state.equals("complete")) {
		    System.out.println("Page is fully loaded");
		}

//		Open an Alert Box
		js.executeScript("alert('Hi Bhupi, your script is 🔥');");

//		Zoom In or Out on the Page
		js.executeScript("document.body.style.zoom='50%'");  // Zoom out
		js.executeScript("document.body.style.zoom='150%'"); // Zoom in

//		Remove Element from DOM
		js.executeScript("document.getElementById('annoying-popup').remove();");

//		Set Attribute on Element
		WebElement element2 = driver.findElement(By.id("myinput"));
		js.executeScript("arguments[0].setAttribute('value','Hello')", element2);
//		Modifying Element Attributes
		// Enable a disabled input field
		js.executeScript("document.getElementById('disabledField').disabled = false;");
		// Change the value of an input
		js.executeScript("document.getElementById('email').value = 'test@example.com';");
		// Hide an element
		js.executeScript("arguments[0].style.visibility='hidden';", element);

//		Asynchronous Operations with executeAsyncScript
		// Wait for a 3-second AJAX call to complete
		String script =
		    "var callback = arguments[arguments.length - 1];" +
		    "setTimeout(function() { callback('Done!'); }, 3000);";

		String result = (String) js.executeAsyncScript(script);
		System.out.println(result); // Prints "Done!"
		
//		Simulating Complex Interactions
		String script1 =
			    "var source = arguments[0], target = arguments[1];" +
			    "var event = new MouseEvent('mousedown', { bubbles: true });" +
			    "source.dispatchEvent(event);" +
			    "event = new MouseEvent('mousemove', { bubbles: true });" +
			    "target.dispatchEvent(event);" +
			    "event = new MouseEvent('mouseup', { bubbles: true });" +
			    "target.dispatchEvent(event);";

			js.executeScript(script1, element, element);
			
//			Frame & Navigation Hacks
			// Switch into an iframe via JS (works even if traditional switchTo() borks)
			js.executeScript(
			  "window.frameElement && window.frameElement.id ? " +
			  "window.alert('Already in frame!') : " +
			  "document.getElementById('payment_iframe').contentWindow.focus();"
			);

			// Push a new history state without reload (deep-link testing)
			js.executeScript("window.history.pushState({}, '', '/new/dashboard');");

	}

}
