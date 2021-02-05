class Singleton {
    private:
        //cannot be accessed error on line 10. 
        Singleton(Singleton const&);
 
    public:
        Singleton() = default;
        //better error messges
        Singleton(Singleton const&) = delete;
        Singleton operator=(Singleton const&) = delete;

        static Singleton getInstance(){
            static Singleton instance;
            return instance; 
        }
    
        

    
};