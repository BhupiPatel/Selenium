package allSeleniumMethods;

import java.io.File;
import java.io.IOException;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Keys;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.Point;
import org.openqa.selenium.Rectangle;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver.Navigation;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.io.FileHandler;

public class AllMethods {

	@SuppressWarnings({ "deprecation", "unused" })
	public static void main(String[] args) throws IOException {
		ChromeDriver driver=new ChromeDriver();
		driver.get("");
		driver.getTitle();
		driver.getCurrentUrl();
		driver.getNetworkConditions();
		driver.getPageSource();
		driver.close();
		driver.quit();
		
//		SwitchTo
//		windowHandels
		String s=driver.getWindowHandle();
		Set<String> allWin=driver.getWindowHandles();
		ArrayList<String> a=new ArrayList<String>(driver.getWindowHandles());
//		window
		driver.switchTo().window(a.get(0));
		driver.switchTo().window(a.get(1));
//		Alert
		Alert al=driver.switchTo().alert();
		al.accept();
		al.dismiss();
		al.getText();
		driver.switchTo().activeElement();
		driver.switchTo().alert();
		driver.switchTo().alert().accept();
		driver.switchTo().alert().dismiss();
		driver.switchTo().alert().getText();
		driver.switchTo().alert().sendKeys("");
		
//		iFrame
		driver.switchTo().frame(0);
		driver.switchTo().frame("");
		driver.switchTo().frame(driver.findElement(By.xpath("")));
		driver.switchTo().defaultContent();
		
		Navigation nav=driver.navigate();
		nav.back();
		nav.forward();
		nav.refresh();
		nav.to("");
		driver.navigate().back();
		driver.navigate().forward();
		driver.navigate().refresh();
		driver.navigate().to(""); //Internally calls get() method
		
//		Manage.cookies
		driver.manage().addCookie(null);
		driver.manage().deleteAllCookies();
		driver.manage().deleteCookie(null);
		driver.manage().deleteCookieNamed("");
		driver.manage().getCookieNamed("");
		driver.manage().getCookies();
		driver.manage().logs();
//		Manage.window
		driver.manage().window().fullscreen();
		driver.manage().window().maximize();
		driver.manage().window().minimize();
		Point p=driver.manage().window().getPosition();
		driver.manage().window().setPosition(new Point(0, 0));
		Dimension d=driver.manage().window().getSize();
		driver.manage().window().setSize(new Dimension(0, 0));
//		Manage.timeout
		driver.manage().timeouts();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
		
//		Element (Search Context)
		WebElement e=driver.findElement(By.xpath(""));
		List<WebElement> e2=driver.findElements(By.xpath(""));
		e.click();
		e.clear();
		e.submit();
		
		String text=e.getText();
		String att=e.getAttribute("");
		String css=e.getCssValue("");
		
		Dimension size=e.getSize();
		int hight= size.getHeight();
		int width= size.getWidth();
		Point location=e.getLocation();
		int x=location.getX();
		int y=location.getY();
		Rectangle rect=e.getRect();
		int hightRect= rect.getHeight();
		int widthRect= rect.getWidth();
		int xRect= rect.getX();
		int yRect= rect.getY();
		
		boolean b = e.isDisplayed();
		boolean b1 =e.isEnabled();
		boolean b2 =e.isSelected();
		
		e.sendKeys("Abc");
		e.sendKeys("",Keys.TAB,Keys.ENTER,Keys.chord(Keys.CONTROL,"a"),Keys.chord(Keys.CONTROL,"c"));
		
//		Take SS fullscreen
		TakesScreenshot ts=(TakesScreenshot)driver;
        File source = ts.getScreenshotAs(OutputType.FILE);
        File destination = new File("screenshot.png");
        FileHandler.copy(source, destination);
//      Screenshot of a specific element (not the whole page):
        WebElement element = driver.findElement(By.id("yourElementId"));
        File src = element.getScreenshotAs(OutputType.FILE);
//      Dynamic file names using timestamps:
        String filename = "screenshot_" + System.currentTimeMillis() + ".png";
        File destination1 = new File("screenshots/" + filename);
        FileHandler.copy(src, destination1);
		
	}

}
