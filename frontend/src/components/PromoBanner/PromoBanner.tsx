import './PromoBanner.css'

export default function PromoBanner() {

  const imageURL= "https://scrap-soldier.com"


  return (
    <div className='container'>
      <div className="promo-banner">
        <span>
          <strong>Free US Shipping with purchase of $99 or more</strong>
        </span>
      </div>
      <div className="promo-banner__close">
      </div>
    </div>
  );
}
