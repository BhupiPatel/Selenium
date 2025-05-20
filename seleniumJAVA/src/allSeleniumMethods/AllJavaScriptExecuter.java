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
		
		js.executeScript("window.scrollTo(0, document.body.scrollHeight);");
		js.executeScript("window.scrollTo(0, document.body.scrollHeight);", e);
	}

}
