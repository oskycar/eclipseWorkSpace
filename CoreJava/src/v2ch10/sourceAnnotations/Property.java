package v2ch10.sourceAnnotations; /* Added by AddEclipsePackageName.py */
import java.lang.annotation.*;

@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
public @interface Property
{
   String editor() default ""; 
}
