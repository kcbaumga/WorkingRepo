using System;
using System.IO;

namespace mlmodelsharp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string url = "https://raw.githubusercontent.com/kcbaumga/WorkingRepo/main/Python/mloreilly/datasets/housing/housing.csv";
            System.Net.WebClient client = new System.Net.WebClient();
            byte[] buffer=client.DownloadData(url);
           // string filepath = @"C:home\kyle\Gitrepo\WorkingRepo\CSharp\mlmodelcsharp\calihousing.csv";
           string filepath = @"calihousing.csv";

            Stream stream = new FileStream(filepath, FileMode.Create);
            BinaryWriter write = new BinaryWriter(stream);
            write.Write(buffer);
            stream.Close();
            Console.WriteLine("Completed");
        }
        
    }
}