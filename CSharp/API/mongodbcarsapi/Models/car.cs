using System.Text.Json.Serialization;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace mongodbcarsapi.Models;

public class cardets
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string? Id {get; set; }

    //[BsonElement("Name")]
    //[JsonPropertyName("Name")]
    public double carid { get; set; }
    public string buying{ get; set; } =null!;
    public string maint{ get; set; } =null!;
    public string doors{ get; set; } =null!;
    public string persons{ get; set; } =null!;
    public string lug_boot{ get; set; } =null!;
    public string carsafety{ get; set; } =null!;
    public string decision{ get; set; } =null!;


}
