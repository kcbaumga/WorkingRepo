using System;
using System.Data;
using System.IO;
using Microsoft.ML;
using Microsoft.VisualBasic.FileIO;
//using System.Collections.Generic;
//using Google.Protobuf;
//using Microsoft.ML;
using Reader;

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

            //string CSVFilePathName = @"C:\test.csv";
            string[] Lines = File.ReadAllLines(filepath);
            string[] Fields;
            Fields = Lines[0].Split(new char[] { ',' });
            int Cols = Fields.GetLength(0);
            DataTable dt = new DataTable();
//1st row must be column names; force lower case to ensure matching later on.
            for (int i = 0; i < Cols; i++)
                dt.Columns.Add(Fields[i].ToLower(), typeof(string));
            DataRow Row;
            for (int i = 1; i < Lines.GetLength(0); i++)
            {
                Fields = Lines[i].Split(new char[] { ',' });
                Row = dt.NewRow();
                for (int f = 0; f < Cols; f++)
                    Row[f] = Fields[f];
                dt.Rows.Add(Row);
                
            }

            IDataView dv =  new IDataView(dt);
            //Console.WriteLine(dv.Count);
            Console.WriteLine(dt.Rows.Count);
           // foreach(DataRow dataRow in dt.Rows)
            //{
             //   foreach(var item in dataRow.ItemArray)
              //  {
               //     Console.WriteLine(item);
                //}
           // }
            var mlContext = new MLContext();// Creating the ML.Net IHostEnvironment


            mlContext.Data.TrainTestSplit(dv);
        }
    }
}
//public static void Example()
                //{
            
            //}


            
    