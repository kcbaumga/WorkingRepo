using System;
using System.IO;
using Microsoft.VisualBasic.FileIO;

namespace mlmodelcsharp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string url =
                "https://raw.githubusercontent.com/kcbaumga/WorkingRepo/main/Python/mloreilly/datasets/housing/housing.csv";
            System.Net.WebClient client = new System.Net.WebClient();
            byte[] buffer = client.DownloadData(url);
            // string filepath = @"C:home\kyle\Gitrepo\WorkingRepo\CSharp\mlmodelcsharp\calihousing.csv";
            string filepath = @"calihousing.csv";

            Stream stream = new FileStream(filepath, FileMode.Create);
            BinaryWriter write = new BinaryWriter(stream);
            write.Write(buffer);
            stream.Close();
            Console.WriteLine("Completed");



            // var path = "C//home/kyle/Gitrepo/WorkingRepo/CSharp/mlmodelcsharp/mlmodelcsharp/bin/Debug/calihousing.csv";
            using (TextFieldParser csvParser = new TextFieldParser(@"calihousing.csv"))
            {
                csvParser.CommentTokens = new string[] { "#" };
                csvParser.SetDelimiters(new string[] { "," });
                csvParser.HasFieldsEnclosedInQuotes = true;

                // Skip the row with the column names
                csvParser.ReadLine();

                while (!csvParser.EndOfData)
                {
                    // Read current line fields, pointer moves to the next line.
                    string[] fields = csvParser.ReadFields();
                    string longitude = fields[0];
                    string latitude = fields[1];
                    string housingmedianage = fields[2];
                    string totalrooms = fields[3];
                    string totalbedrooms = fields[4];
                    string population = fields[5];
                    string households = fields[6];
                    string medianincome = fields[7];
                    string medianhousevalue = fields[8];
                    string oceanproximity = fields[9];

                    Console.WriteLine(medianincome);
                }
            }
        }
    }
}