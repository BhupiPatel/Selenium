package all;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

public class AllMethods {
	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","D:\\SW\\chromedriver.exe");
		ChromeDriver d = new ChromeDriver();
		d.get("https://www.google.co.in/");
		d.manage().deleteAllCookies();
		d.close();
		d.quit();
		
//		get
		d.get("");
		String s=d.getCurrentUrl();
		String s1=d.getPageSource();
		String s2=d.getTitle();
		
//		findelements
		d.findElement(By.id(""));
		d.findElement(By.linkText(""));
		d.findElement(By.name(""));
		d.findElement(By.partialLinkText(""));
		d.findElement(By.tagName(""));
		d.findElement(By.className(""));
		d.findElement(By.cssSelector(""));
		d.findElement(By.xpath(""));
		List<WebElement> es=d.findElements(By.xpath(""));
		
		d.findElement(By.xpath("")).click();
		d.findElement(By.xpath("")).submit();
		d.findElement(By.xpath("")).clear();
		d.findElement(By.xpath("")).getAttribute("");
		d.findElement(By.xpath("")).getCssValue("");
		d.findElement(By.xpath("")).getTagName();
		d.findElement(By.xpath("")).getText();
		d.findElement(By.xpath("")).sendKeys("");
		d.findElement(By.xpath("")).sendKeys("",Keys.ENTER,Keys.chord(Keys.CONTROL,"A"));
		
//		switch to
//		frame
		WebElement e=d.findElement(By.linkText(""));
		d.switchTo().frame(0);
		d.switchTo().frame("");
		d.switchTo().frame(e);
		d.switchTo().defaultContent();
		d.switchTo().parentFrame();
		
//		windows
		String ss=d.getWindowHandle();
		ArrayList<String> al=new ArrayList<String>(d.getWindowHandles());
		d.switchTo().window(al.get(0));
		
//		Alart
		d.switchTo().alert().accept();
		d.switchTo().alert().dismiss();
		d.switchTo().alert().getText();
		d.switchTo().alert().sendKeys("");
		
//		active element
		d.switchTo().activeElement().clear();
		d.switchTo().activeElement().click();
		d.switchTo().activeElement().sendKeys("");
		d.switchTo().activeElement().getAttribute("");
		
//		is
		e.isDisplayed();
		e.isEnabled();
		e.isSelected();
		
//		navigat
		d.navigate().to("");
		d.navigate().back();
		d.navigate().forward();
		d.navigate().refresh();
		
//		manage
		d.manage().window().fullscreen();
		d.manage().window().maximize();
		d.manage().window().getSize().getHeight();
		d.manage().window().getSize().getWidth();
		d.manage().window().getPosition().getX();
		d.manage().window().getPosition().getY();
		Dimension dm=new Dimension(00, 00);
		d.manage().window().setSize(dm);
		Point p=new Point(0, 0);
		d.manage().window().setPosition(p);
		
		int i=d.manage().getCookies().size();
		d.manage().deleteAllCookies();
		
		d.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
//		select class
		Select sl=new Select(e);
		
		sl.isMultiple();
		
		sl.selectByIndex(0);
		sl.selectByValue("");
		sl.selectByVisibleText("");
		
		sl.deselectAll();
		sl.deselectByIndex(0);
		sl.deselectByValue("");
		sl.deselectByVisibleText("");
		
		sl.getAllSelectedOptions();
		String ss1=sl.getFirstSelectedOption().getText();
		sl.getOptions();
		
//		Action class
		Actions a=new Actions(d);
		a.click(e).build().perform();
		a.tick(arg0)
		a.sendKeys(e,"").build().perform();
		a.clickAndHold(e).build().perform();
		a.contextClick(e).build().perform();
		a.doubleClick(e).build().perform();
		a.dragAndDrop(e, e).build().perform();
		a.dragAndDropBy(e, 0, 0).build().perform();
		a.moveByOffset(0, 0).build().perform();
		a.moveToElement(e).build().perform();
		a.keyDown("a");
		a.keyUp("a");
		a.pause(5000);
		
//		JavascriptExecutor
		
//		wait state
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}
}
