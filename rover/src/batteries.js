const FULL_LEVEL = 3;
const CHARGE_TIME_MS = 3 * 1000;

class Battery {
  constructor() {
    this.level = FULL_LEVEL;
    this.charging = false;
  }

  isLow() {
    return this.level <= 0;
  }

  use() {
    this.level--;
  }

  charge() {
    if (this.charging) return;

    this.charging = true;
    setTimeout(() => {
      this.level = FULL_LEVEL;
      this.charging = false;
    }, CHARGE_TIME_MS);
  }
}

exports.createBattery = () => new Battery();
