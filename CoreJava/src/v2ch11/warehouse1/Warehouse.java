package v2ch11.warehouse1; /* Added by AddEclipsePackageName.py */
import java.rmi.*;

/**
   The remote interface for a simple warehouse.
   @version 1.0 2007-10-09
   @author Cay Horstmann
*/
public interface Warehouse extends Remote
{  
   double getPrice(String description) throws RemoteException;
}
