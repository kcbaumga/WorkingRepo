using mongodbcarsapi.Models;
using Microsoft.Extensions.Options;
using MongoDB.Driver;

namespace mongodbcarsapi.Services;
public class carsService
{
    private readonly IMongoCollection<cardets> _carsCollection;
    public carsService(
       IOptions<cardatabasesettings> carStoreDatabaseSettings) 
       {
        var mongoClient = new MongoClient(
            carStoreDatabaseSettings.Value.ConnectionString);

        var mongoDatabase = mongoClient.GetDatabase(
            carStoreDatabaseSettings.Value.DatabaseName);

        _carsCollection = mongoDatabase.GetCollection<cardets>(
            carStoreDatabaseSettings.Value.BooksCollectionName);
       }
    public async Task<List<cardets>> GetAsync() =>
    await _carsCollection.Find(_ => true).ToListAsync();

    public async Task<cardets?> GetAsync(string id) =>
        await _carsCollection.Find(x => x.Id == id).FirstOrDefaultAsync();

    public async Task CreateAsync(cardets newCar) =>
        await _carsCollection.InsertOneAsync(newCar);

    public async Task UpdateAsync(string id, cardets updatedCar) =>
        await _carsCollection.ReplaceOneAsync(x => x.Id == id, updatedCar);

    public async Task RemoveAsync(string id) =>
        await _carsCollection.DeleteOneAsync(x => x.Id == id);
    
}